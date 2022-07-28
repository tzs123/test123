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
import time,csv,os,re
import requests

base_path = os.path.dirname(os.path.dirname(__file__)) #项目基本路径
case_path = os.path.join(base_path,'testcase')  #测试脚本所在目录
data_path = os.path.join(base_path,'data')  #测试用例所在的目录
report_path = os.path.join(base_path,'report')  #测试报告所在目录

def request(url,method,data=None,header=None):
    '''根据不同的请求方法对接口发起请求'''
    rq = requests.session()  #创建session对象
    if method in ('get','GET','Get'):
        r = rq.get(url=url,params=data,header=header)
    elif method in ('POST','post','Post'):
        r = rq.post(url=url,data=data)
    return r

def get_time():
    t = time.strftime('%Y-%m-%d %X')
    return t

def read_csv(file):
    if os.path.exists(file):
        file_csv = open(file,'r')
        rows = csv.reader(file_csv)
        return list(rows)
    else:
        print(f'文件{file}不存在')
        return False

def get_test_data(s):
    '''
    将’account=admin,\npassword=123456'格式字符串转换为字典{'account':'admin','password':'123456'}
    :param s:
    :return:
    '''
    data = {}
    r = re.split(',\n',s)  #['account=admin','password=123456']
    for i in r:
        key = i.split('=')[0]  # ['account','admin']
        value = i.split('=')[1]
        data[key] = value
    return data

# if __name__ == '__main__':
#     dd = read_csv(data_path + '/login_data.csv')
#     print(dd[7:][0][1])
#     print(eval(dd[7:][0][1])['account'])
