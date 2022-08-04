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
import os
import allure
import sys
# from common.request import HTTPHandle
import pytest

sys.dont_write_bytecode = True


# @allure.epic('测试描述'.center(30, '*'))
# @allure.feature('生肖')       #模块
# class TestPytestOne():
#     @allure.story('用户故事描述：生肖配对')      #模块的功能
#     @allure.description('测试标题：生肖配对')
#     @allure.title('测试用例描述：生肖配对')
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_02(self,action):
#         url = 'http://apis.juhe.cn/sxpd/query'
#         req = HTTPHandle().visit(method='get',
#                                  url=url,
#                                  headers=None,
#                                  params={
#                                      'men': '狗',
#                                      'women':'鼠',
#                                      'key':'165a0b380d7ffcc86a8e1e545b4e79e0'
#                                  })
#         res = json.dumps(req, ensure_ascii=False)
#         print(res)
        # print(req['result'])
        # with allure.step("请求"):
        #     allure.attach('{}'.format(url),name='get请求')
        # with allure.step("响应"):
        #     allure.attach('{}'.format(res),name='返回结果')
        # with allure.step("断言"):
        #     assert res == excel[0]['except']
        #     allure.attach('OK',name='断言成功')
class TestPytestOne():
    @allure.story('用户故事描述：用例二')
    @allure.title('测试标题：用例二')
    @allure.description('测试用例描述：用例二')
    @allure.testcase('测试用例地址:http://www.sogou.com/')
    @allure.tag('测试用例标签：用例二')
    # @pytest.mark.skip(reason='本次不执行')
    # @allure.severity(allure.severity_level.MINOR)
    def test_01(self):
        print('执行第二个用例')
        with allure.step("断言"):
            assert 1 == 1
        allure.attach('OK',name='断言成功')

    @allure.story('用户故事描述：用例二')
    @allure.title('测试标题：用例二')
    @allure.description('测试用例描述：用例二')
    @allure.testcase('测试用例地址:http://www.sogou.com/')
    @allure.tag('测试用例标签：用例二')
    def test_02(self):
        print('---用例01---')
        assert 1 == 1

    @allure.story('用户故事描述：用例二')
    @allure.title('测试标题：用例二')
    @allure.description('测试用例描述：用例二')
    @allure.testcase('测试用例地址:http://www.sogou.com/')
    @allure.tag('测试用例标签：用例二')
    def test_03(self):
        print('---用例02---')
        assert 1 == 1



if __name__ == '__main__':
    pytest.main(['pytest test_demo.py --alluredir=./report/tmp --clean-alluredir'])
    os.system("allure generate ./report/tmp -o report/html --clean")
    os.system('allure serve ./report/tmp')

