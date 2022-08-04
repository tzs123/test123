# _*_ coding:utf-8 _*_

import json
import unittest
from middleware import helper
from common import ddt
from common.RequestHandler import HTTPHandler
from common.excel_handler import ExcelHandler
from run_case import logger
from common.DBhandler import MysqlUtil


@ddt.ddt
class Test_Register(unittest.TestCase):
    # 读取测试数据
    excel_handle = ExcelHandler(os.path.join(dir_config.testdatas_dir, "data.xlsx"))
    test_data = excel_handle.read_key_value("register")

    def setUp(self) -> None:
        self.req = HTTPHandler()
        self.db_info = ReadYaml(dir_config.yaml_dir, 'db_info').get_data()
        self.db = MysqlUtil(self.db_info)
        self.host = ReadYaml(dir_config.yaml_dir, 'ApiHost').get_data()['mockhost']

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*test_data)
    def test_charge(self, test_data):
        # 判断excel中是否 出现了 #new_phone# ，如果出现，随机生成一个，进行替换
        if '#new_phone#' in str(test_data["json"]):
            while True:
                mobilephone = helper.gen_phonenun()
                sql1 = '''SELECT *  FROM users WHERE phonenum = %s ;'''
                dbphone = self.db.query(sql=sql1, args=mobilephone)
                if not dbphone:
                    break
            test_data["json"] = test_data["json"].replace('$new_phone$', mobilephone)

        # 判断excel中是否 出现了 $exist_phone$ ，如果出现，随机生成一个，进行替换
        if '#exist_phone#' in str(test_data["json"]):
            sql2 = '''select phonenum from users limit 1;'''
            mobilephone = self.db.query(sql=sql2)["phonenum"]
            test_data["json"] = test_data["json"].replace('$exist_phone$', mobilephone)

        sql = '''SELECT money from memberinfo where memberid = %s;'''
        # 查询用户账户初始金额
        before_money = self.db.query(sql, args=[self.memberid])

        # 判断excel中是否 出现了 #memberid# ，如果出现，进行替换
        if '#memberid#' in str(test_data["json"]):
            test_data["json"] = test_data["json"].replace('#memberid#', str(self.memberid))

        # 读取excel中的headers数据（字典类型）
        headers = json.loads(test_data["headers"])
        # 添加token信息
        if headers['token'] == '#token#':
            headers['token'] = self.token


        self.logger.info("用例名称：{};接口信息：url={}；method={}；headers={}；json={}".format(test_data["case_name"],
                                                                                   self.host + test_data["url"],
                                                                                   test_data["method"],
                                                                                   json.loads(headers),
                                                                                   json.loads(test_data["json"])
                                                                                   )
                         )

        res = self.req.visit(
            url=self.host + test_data["url"],
            method=test_data["method"],
            headers=json.loads(headers),
            json=json.loads(test_data["json"])
        )
        self.logger.info("接口响应内容：{}".format(res))

        # 错误处理，抛出异常
        try:
            self.assertEqual(res["code"], test_data["excepted"])
            self.logger.info("接口响应code:{}，期望响应code:{}".format(res["code"], test_data["excepted"]))
            # 写入实际结果到excel表格
            self.excel_handle.write_change(helper.Context.excelpath,
                                           "register",
                                           test_data["caseid"] + 1, 9, "passed")

        except AssertionError as e:
            self.logger.error("测试用例执行失败：{}".format(e))
            self.excel_handle.write_change(helper.Context.excelpath,
                                           "register",
                                           test_data["caseid"] + 1, 9, "failed")
            raise e

        if res['code'] == "0000":
            charge_money = json.loads(test_data["json"])["chargeinfo"]["chargeMoney"]
            # 查询用户账户充值后的金额
            after_money = self.db.query(sql, args=[self.memberid])
            self.logger.info("用户账户初始金额:{}，充值金额:{}，用户账户充值后的金额:{}".format(before_money, charge_money, after_money))
            self.assertEqual(before_money + charge_money, after_money)

