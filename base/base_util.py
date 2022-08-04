# _*_ coding:utf-8 _*_

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



class BasePage:
    def __init__(self,driver):
        # 打开浏览器
        self.driver = driver

    def visit(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    #定位元素关键字
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    #设置值的关键字
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    #单击关键字
    def click(self,loc):
        self.locator_element(loc).click()

    #进入框架关键字
    def goto_frame(self,frame_name):
        self.driver.switch_to_frame(frame_name)

    #出框架关键字
    def quit_frame(self):
        self.driver.switch_to_default_content()

    #封装下拉框关键字
    def choice_select(self,loc,value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    #获取文本的值
    def get_value(self,loc):
        return self.locator_element(loc).text

    def handle(self,loc):
        #获取当前窗口句柄
        current_handle = self.driver.current_window_handle
        self.driver.switch_to_window(current_handle)
        self.click(loc)
        #隐式等待10s
        self.driver.implicitly_wait(10)
        #获取当前所有窗口句柄
        allhandles = self.driver.window_handles
        for handles in allhandles:
            if handles != current_handle:
                self.driver.switch_to_window(handles)

    #鼠标悬浮在标签上面，用于web操作，相当于拖拽
    def ActionChains(self,loc):
        ele = self.locator_element(loc).click()
        ActionChains(self.driver).move_to_element(ele).perform()


    def touchactions(self,loc):
        #定位要滑动的年、月、日，用于app操作，拖拽
        dwnwos = self.locator_element(loc)
        year = dwnwos[0]
        month = dwnwos[1]
        day = dwnwos[2]
        action = webdriver.TouchActions(self.driver)
        action.scroll_from_element(year,0,5).perform()
        action.scroll_from_element(month, 0, 30).perform()
        action.scroll_from_element(day, 0, 30).perform()

    #窗口截图
    def save_screenshot(self,path):
        self.driver.save_screenshot(path)
        #例如path=“./files/baidu_img.png”

    #调用JavaScript（浏览器滚动条）
    def windows_scroll(self):
        js = "window.scrollTo(0,4550)"
        self.driver.execute_script(js)

    #获取警告框
    def switch_to_alert(self,loc):
        self.locator_element(loc).click()
        alert = self.driver.switch_to_alert()
        alert.accept()

    #通过cookie绕过登录
    def cookie(self,name,value,name1,value1):
        self.driver.add_cookie({'name':name,'value':value})
        self.driver.add_cookie({'name': name1, 'value': value1})
        time.sleep(2)
        self.driver.refresh()
