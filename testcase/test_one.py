# _*_ coding:utf-8 _*_
import json

import allure
import pymysql

from common.excel_util import excel


@allure.epic('测试描述'.center(30, '*'))
@allure.feature('数据库')       #模块
class Testmysql():
    @allure.story('用户故事描述：查询数据')  # 模块的功能
    @allure.description('测试描述：查询数据是否正确')
    @allure.title('测试用例描述：查询客户数据')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_03(self,action):
        db = pymysql.connect(host = '192.168.0.219',port =3306,db='test',user='root',passwd='123',charset='utf8')
        info = db.cursor()
        info.execute('select id,username from sec_custinfo')
        data = info.fetchall()
        ret =[]
        for one,two in data:
            line = one
            line1 = two
            ret.append([line,line1])
        print(ret)
        #结果：[['1', '董卓'], ['2', '张坤'], ['3', '王伟']]
        with allure.step("查询"):
            allure.attach('select id,username from sec_custinfo',name='sql执行')
        with allure.step("响应"):
            allure.attach('{}'.format(ret),name='返回结果')
        with allure.step("断言"):
            assert ret[0] == ['1', '董卓']
            allure.attach('OK',name='断言成功')
