# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test1111.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''
import json
import os

import pytest
import requests
import allure
import sys

from common.request import HTTPHandle

sys.dont_write_bytecode = True


@allure.epic('测试描述'.center(30, '*'))
@allure.feature('测试模块')
@allure.suite('测试套件')
class TestPytestOne():
    @allure.story('用户故事描述：用例一')
    @allure.title('测试标题：用例一')
    @allure.description('测试用例描述：用例一')
    @allure.testcase('测试用例地址:http://www.baidu.com/')
    @allure.tag('测试用例标签：用例一')
    def test_one(self):
        req = HTTPHandle().visit(method='get',
                                 url='http://web.juhe.cn/constellation/getAll',
                                 headers=None,
                                 params={
                                     'consName': '天蝎座',
                                     'type': 'year',
                                     'key': '8ffc14ff3cc065d7e76d122975f9517b'
                                 })
        res = json.dumps(req, ensure_ascii=False)
        print(res)

    @allure.story('用户故事描述：用例二')
    @allure.title('测试标题：用例二')
    @allure.description('测试用例描述：用例二')
    @allure.testcase('测试用例地址:http://www.sogou.com/')
    @allure.tag('测试用例标签：用例二')
    def test_two(self):
        print('执行第二个用例')
        assert True == True


# pytest运行
if __name__ == "__main__":
    pytest.main(['test_Demo.py', '-s','-q', '--alluredir', '../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/html --clean')

