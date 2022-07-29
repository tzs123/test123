# coding:utf-8

import pytest
import os
from common.Email_manage import EmailManage
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

if __name__ == "__main__":
    #生成json临时文件
    pytest.main(['-vs','../testcase','--alluredir','../temp','--clean-alluredir'])
    # #根据json临时文件生成allure报告
    os.system('allure generate  ../temp -o ../report  --clean')
    # EmailManage().send_email(r'测试报告地址：http://192.168.8.100:63342/untitled/report/index.html?_ijt=urb3ar4qs64bm6laiivmfj4ue1<br> 请在收到邮件后三十分钟内查看！"')
    suite = unittest.defaultTestLoader.discover('../venv/', '*.py')
    files = open('../report/index.html', 'wb')
    runner = HTMLTestRunner(stream=files,title='申万项目自动化测试报告',description='报告描述')
    runner.run(suite)
    files.close()
    time.sleep(3)
    EmailManage().send_email(files.name)
