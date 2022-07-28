# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test_login.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pageobject.login_page import LoginPage
class AccountPage(BasePage):

    #账户余额
    account_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/div/ul[2]/li[3]/a')
    assert_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/ul/li[1]/a')

    def test_account(self):
        self.click(self.account_loc)
        self.driver.implicitly_wait(10)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        self.driver.implicitly_wait(10)
        assert self.get_value(self.assert_loc) == '充值记录'
        print('进入账户余额')
