# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test_two.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''
import json
import allure
import sys

sys.dont_write_bytecode = True

@allure.story('用户故事描述：用例二')
@allure.title('测试标题：用例二')
@allure.description('测试用例描述：用例二')
@allure.testcase('测试用例地址:http://www.sogou.com/')
@allure.tag('测试用例标签：用例二')
# @pytest.mark.skip(reason='本次不执行')
@allure.severity(allure.severity_level.MINOR)
def test_01():
    print('执行第二个用例')
    with allure.step("断言"):
        assert 1 == 1
        allure.attach('OK',name='断言成功')

