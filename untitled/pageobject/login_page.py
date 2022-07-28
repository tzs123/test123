#coding:utf-8
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base.base_page import BasePage
from common.yanl_handler import YamlHandler


class LoginPage(BasePage):

    #登录
    username_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    password_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    Verification_loc =(By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div/div[3]/input')
    submit_loc = (By.NAME,'sbtbutton')
    assert_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/h1')
    url = 'http://testingedu.com.cn:8000/index.php/Home/user/login.html'
    alter_loc = (By.XPATH,'/html/body/div[6]/div[3]/a')

    def test_login(self,username,password,Verification):
        try:
            self.driver.get(self.url)
            self.clear(self.Verification_loc)
            self.clear(self.username_loc)
            self.send_keys(self.username_loc,username)
            self.clear(self.password_loc)
            self.send_keys(self.password_loc,password)
            self.clear(self.Verification_loc)
            self.send_keys(self.Verification_loc,Verification)
            self.click(self.submit_loc)
            if username == '13800138006' and password == '123456' and Verification == '123':
                # 断言
                assert self.get_value(self.assert_loc) == '我的订单'
                self.driver.implicitly_wait(20)
                allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
            else:
                # 点击弹框
                self.click(self.alter_loc)
                self.driver.implicitly_wait(20)
                allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

        except ValueError:
            pass



# if __name__ == '__main__':
#     aa = LoginPage(webdriver.Chrome())
#     aa.test_login()


