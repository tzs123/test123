# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure
import pytest
@allure.story('用户故事描述：用例二')
@allure.title('测试标题：用例二')
@allure.description('测试用例描述：用例二')
@allure.testcase('测试用例地址:http://www.sogou.com/')
@allure.tag('测试用例标签：用例二')
@pytest.mark.smoke
def test2():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()