#coding:utf-8
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):

    #页面元素
    url = "http://pledge-risk-web.k8s-dev.kingdomai.com"
    username_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[2]/span/input')
    password_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[3]/span/input')
    Verification_loc =(By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[4]/div/span/input')
    submit_loc = (By.XPATH,'//*[@id="wrap"]/div/div[2]/div/div[5]')
    # tuichu_loc = (By.LINK_TEXT,'')
    #页面的动作
    def login_ecshop(self,username,password,Verification):
        # self.send_keys(LoginPage.username_loc,username)
        # self.send_keys(LoginPage.password_loc,password)
        # self.send_keys(LoginPage.Verification_loc,Verification)
        # self.click(LoginPage.submit_loc)
        self.visit(self.url)
        self.send_keys(self.username_loc, username)
        self.send_keys(self.password_loc, password)
        self.send_keys(self.Verification_loc, Verification)
        self.click(self.submit_loc)

    #断言
    # def get_except_result(self):
    #     self.goto_frame('')
    #     return self.get_value(LoginPage.tuichu_loc)

# if __name__ == '__main__':
#     LoginPage().login_ecshop('wzy','123456','x565')