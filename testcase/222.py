# _*_ coding:utf-8 _*_
import time

import pytest
from appium import webdriver



class Test:
    def setup(self):
        desired_caps = {"deviceName": '127.0.0.1:62001',
                        'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'appPackage': 'com.android.launcher3',
                        'appActivity': '.launcher3.Launcher',
                        'unicodekeyboard': True,
                        'resetkeyboard': True
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@text="QQ音乐"]').click()
        self.driver.implicitly_wait(20)
    @pytest.mark.parametrize('name',["11"])
    def test1(self,name):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/ce8"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/eng"]').clear()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/eng"]').send_keys(name)
        self.driver.implicitly_wait(20)
        self.driver.keyevent(66)#66代表键盘enter
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/epe"]').click()
        self.driver.implicitly_wait(20)
        name = self.driver.find_element_by_xpath('//*[@content-desc="歌手: 11"]').text
        assert '11' in name
        print('111111111111')
        self.driver.keyevent(4)

    def teardown(self):
        self.driver.quit()