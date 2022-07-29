# coding:utf-8
import json
import os
import time
import unittest

import allure

import jsonpath
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from HTMLTestRunner import HTMLTestRunner

from common.Email_manage import EmailManage
from common.excel_util import ExcelHandler, excel
from common.loger_handler import logger
from common.request import HTTPHandle
from common.sql_util import sql

from pageobject.login_page import LoginPage


class TestLogin:

    @pytest.mark.parametrize("username,password,Verification",ExcelHandler(r'D:\pychramproject\python\untitled\data\logindata.xlsx').ui_read('login'))
    def test_01_login(self,username,password,Verification):
        """登录"""
        lp = LoginPage()
        # 输入用户名和密码,验证码
        lp.login_ecshop(username,password,Verification)
        # 断言
        # assert  lp.get_except_result()=='退出'

    def test_02_login(self):
        # resList = ExcelHandler(r'D:\pychramproject\python\untitled\data\login_data.xlsx')
        # res = req  # 传入对应行的请求
        # # print(res)
        # ress = json.loads(res.text)
        # print(ress)
        # 3-实际与预期相对比，结果写入测试结果到excel----做判断--断言
        for i in range(0,4):
            try:
                req = HTTPHandle().visit(method=excel[i]['method'],
                                                   url=excel[i]['url'],
                                                   headers=json.loads(excel[i]['headers']),
                                                   data=excel[i]['data'])
                ress = json.loads(req.text)
                # print(ress)
                logger.info('*'*88)
                logger.info("这是第{0}条用例：{1}".format(excel[i]['case_id'],excel[i]['title']))
                logger.info(ress)
                if ress['message'] == excel[i]['expected_result']:   #跟期望值对比
                    # if ress['msg_code'] == int((sql[1])[0][4]):               #跟查询结果对比
                    # 写入成功！
                        ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx','login', i+2, 10,'pass')  # workSheetNew.write(行号，列号，值)
                        ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx', 'login', i+2, 9,ress['code'])
                        ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx', 'login', i + 2, 8,ress['message'])
                else:
                    # 写入没有成功！
                    ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx','login', i+2, 10,'fail') # workSheetNew.write(行号，列号，值)
                    ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx', 'login', i + 2, 9, ress['code'])
                    ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx', 'login', i + 2, 8, ress['message'])
            except Exception as e:
                logger.info('*' * 88)
                logger.info(
                    "这是第{0}条用例：{1}".format(excel[i]['case_id'], excel[i]['title']))
                logger.info(e)
                ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx', 'login', i + 2, 10,
                              'fail')  # workSheetNew.write(行号，列号，值)
                ExcelHandler.write(r'D:\pychramproject\python\untitled\data\login_data.xlsx', 'login', i + 2, 8, str(e))
                pass
            continue

