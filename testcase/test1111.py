# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test1111.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

@allure.epic("xxx测试")
@allure.feature("登录模块")
class Test:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @allure.story("登录")
    def test1(self,login):
        #输入账号，密码
        self.driver.find_element_by_id("username").send_keys('13800138006')
        self.driver.find_element_by_id("password").send_keys('123456')
        while True:
            try:
                acode = int(input('请输入验证码:'))
                self.driver.find_element_by_id('verify_code').send_keys(acode)
                self.driver.find_element_by_name(
                    'sbtbutton').click()
                # assert self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/a[1]').text()=="Stephen11111"
                break
            except:
                print("验证码不能为空")
                continue
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
        #鼠标光标悬浮在标签上
        ele = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/a')
        ActionChains(self.driver).move_to_element(ele).perform()
        ele1 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[1]/h3/div/a')
        ActionChains(self.driver).move_to_element(ele1).perform()
        current_handle = self.driver.current_window_handle
        self.driver.switch_to_window(current_handle)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/dl[1]/dd/a[6]').click()
        # 隐式等待10s
        self.driver.implicitly_wait(10)
        # 获取当前所有窗口句柄
        allhandles = self.driver.window_handles
        for handles in allhandles:
            if handles != current_handle:
                self.driver.switch_to_window(handles)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/a/img').click()
    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['test1111.py', '-s', '-q', '--alluredir', './report'])
    os.system('allure generate report -o report/html --clean')