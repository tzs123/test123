# coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_util import BasePage


class ProductManagePage(BasePage):

    #页面元素
    product_list_loc = (By.XPATH,'/html/body/div[1]/div/section/section/aside/div/ul/li[1]/ul/li[2]')
    cat_id_loc = (By.XPATH,'/html/body/div[1]/div/section/section/main/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/span/input')
    sousuo_loc = (By.XPATH,'/html/body/div[1]/div/section/section/main/div/div[2]/div/div/div[2]/div/div[8]/button/span')
    #页面动作

    def select_product(self,aaa):

        # self.goto_frame('')
        # self.click(ProductManagePage.product_list_loc)
        # self.quit_frame()
        # self.goto_frame('')
        # self.choice_select(ProductManagePage.cat_id_loc,'')
        # self.click(ProductManagePage.sousuo_loc)
        # self.visit(self.url)
        self.click(self.product_list_loc)
        time.sleep(2)
        self.send_keys(self.cat_id_loc,aaa)
        self.click(self.sousuo_loc)