# coding:utf-8
from selenium import webdriver


class BaseUtil:
    def setup(self) -> None:
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 加载页面
        self.driver.get("http://pledge-risk-web.k8s-dev.kingdomai.com")

    def teardown(self) -> None:
        pass