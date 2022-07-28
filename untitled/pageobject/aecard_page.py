# coding:utf-8
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage



class AecardPage(BasePage):

    #积分商城
    aecard_loc = (By.XPATH,'/html/body/div[2]/div/div[3]/ul/li[4]/a')
    assert_loc = (By.XPATH,'/html/body/div[2]/div/div[1]/span')

    def test_aecard(self):
        self.click(self.aecard_loc)
        self.driver.implicitly_wait(10)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        self.driver.implicitly_wait(10)
        assert self.get_value(self.assert_loc) == '积分商城'
        print('进入积分商城')



