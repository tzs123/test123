# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test_two.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''
import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from common.excel_util import excel


@allure.epic("xxx测试")
@allure.feature("登录模块")
class Test:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：正确的账号密码登录成功')
    @allure.title('测试用例描述：正确的账号密码登录成功')
    # @pytest.mark.parametrize("username,password,verify_code",[(1,2,2),(2,5,6)])
    def test_04(self,action):
        # while True:
        #     for i in range(4):
        #         try:
        #
        #             with allure.step("输入账号"):
        #                 allure.attach('{}'.format(excel[i]['username']), name='账号')
        #             self.driver.find_element_by_id("verify_code").clear()
        #             time.sleep(2)
        #             self.driver.find_element_by_id("username").clear()
        #             self.driver.find_element_by_id("username").send_keys(excel[i]['username'])
        #             with allure.step("输入密码"):
        #                 allure.attach('{}'.format(excel[i]['password']), name='密码')
        #             self.driver.find_element_by_id("password").clear()
        #             self.driver.find_element_by_id("password").send_keys(excel[i]['password'])
        #             with allure.step("输入验证码"):
        #                 allure.attach('{}'.format(excel[i]['verify_code']), name='验证码')
        #             self.driver.find_element_by_id("verify_code").clear()
        #             self.driver.find_element_by_id('verify_code').send_keys(excel[i]['verify_code'])
        #             # self.driver.find_element_by_name(
        #             #     'sbtbutton').click()
        #             current_handle = self.driver.current_window_handle
        #             self.driver.switch_to_window(current_handle)
        #             self.driver.find_element_by_name(
        #                 'sbtbutton').click()
        #             # 隐式等待10s
        #             self.driver.implicitly_wait(10)
        #             allhandles = self.driver.window_handles
        #             for handles in allhandles:
        #                 if handles != current_handle:
        #                     self.driver.switch_to_window(handles)
        #             self.driver.find_element_by_class_name('layui-layer-btn0').click()
        #             allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        #             self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
        #             break
        #         except:
        #             continue
        #     break
        with allure.step("输入正确账号"):
            allure.attach('{}'.format('13800138006'),name='正确账号')
        self.driver.find_element_by_id("username").send_keys('13800138006')
        with allure.step("输入正确密码"):
            allure.attach('{}'.format('123456'),name='正确密码')
        self.driver.find_element_by_id("password").send_keys('123456')
        with allure.step("输入正确验证码"):
            allure.attach('{}'.format('123'),name='正确验证码')
        self.driver.find_element_by_id('verify_code').send_keys('123')
        self.driver.find_element_by_name(
            'sbtbutton').click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

        # while True:
        #     try:
        #         acode = int(input('请输入验证码:'))
        #         self.driver.find_element_by_id('verify_code').send_keys(acode)
        #         self.driver.find_element_by_name(
        #             'sbtbutton').click()
        #         # assert self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/a[1]').text()=="Stephen11111"
        #         break
        #     except:
        #         print("验证码不能为空")
        #         continue
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
        # #鼠标光标悬浮在标签上
        # time.sleep(2)
        # ele = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/a')
        # ActionChains(self.driver).move_to_element(ele).perform()
        # ele1 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[1]/h3/div/a')
        # ActionChains(self.driver).move_to_element(ele1).perform()
        # current_handle = self.driver.current_window_handle
        # self.driver.switch_to_window(current_handle)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/dl[1]/dd/a[6]').click()
        # # 隐式等待10s
        # self.driver.implicitly_wait(10)
        # # 获取当前所有窗口句柄
        # allhandles = self.driver.window_handles
        # for handles in allhandles:
        #     if handles != current_handle:
        #         self.driver.switch_to_window(handles)
        # self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/a/img').click()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：错误的账号登录失败')
    @allure.title('测试用例描述：错误的账号登录失败')
    def test_05(self):
        with allure.step("输入错误账号"):
            allure.attach('{}'.format('12312345123'),name='错误账号')
        self.driver.find_element_by_id("username").send_keys('12312345123')
        with allure.step("输入正确密码"):
            allure.attach('{}'.format('123456'),name='正确密码')
        self.driver.find_element_by_id("password").send_keys('123456')
        with allure.step("输入正确验证码"):
            allure.attach('{}'.format('123'),name='正确验证码')
        self.driver.find_element_by_id('verify_code').send_keys('123')
        self.driver.find_element_by_name(
            'sbtbutton').click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：错误的密码登录失败')
    @allure.title('测试用例描述：错误的密码登录失败')
    def test_06(self):
        with allure.step("输入正确账号"):
            allure.attach('{}'.format('13800138006'),name='正确账号')
        self.driver.find_element_by_id("username").send_keys('13800138006')
        with allure.step("输入错误密码"):
            allure.attach('{}'.format('123'),name='错误密码')
        self.driver.find_element_by_id("password").send_keys('123')
        with allure.step("输入正确验证码"):
            allure.attach('{}'.format('123'),name='正确验证码')
        self.driver.find_element_by_id('verify_code').send_keys('123')
        self.driver.find_element_by_name(
            'sbtbutton').click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：错误的验证码登录失败')
    @allure.title('测试用例描述：错误的验证码登录失败')
    def test_07(self):
        with allure.step("输入正确账号"):
            allure.attach('{}'.format('13800138006'),name='正确账号')
        self.driver.find_element_by_id("username").send_keys('13800138006')
        with allure.step("输入正确密码"):
            allure.attach('{}'.format('123456'),name='正确密码')
        self.driver.find_element_by_id("password").send_keys('123456')
        with allure.step("输入错误验证码"):
            allure.attach('{}'.format(''),name='验证码为空')
        self.driver.find_element_by_id('verify_code').send_keys('')
        self.driver.find_element_by_name(
            'sbtbutton').click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    def teardown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     pytest.main(['-s','test_one.py','test_two.py','test_Demo.py'])