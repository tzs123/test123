# _*_ coding:utf-8 _*_

'''
@auth:tzs
@date:2022/4/13
'''
import os

import jinja2
import pytest
import yaml
from jinja2 import Template

from common.yanl_handler import yaml_data

from string import Template

import yaml


def yaml_template(data: dict):
    with open("../config/bbb.yaml", encoding="utf-8") as f:
       #  f.read()读取的是yaml文件的文本格式数据（即读取出来的数据为字符串格式）
       #  这里代码的作用是将data数据替换f.read()读出来的$标识的数据---简单来说就是读取yaml文件中的数据，然后替换原数据中被$符号标识的变量，得到新的数据（此时没有生成新的对象，只是改变了数据的内容）
        re = Template(f.read()).substitute(data)

        print(re, type(re))
        # method: get
        # url: http: // www.baidu.com
        # headers:
        #     Content - Type: application / json
        #     token: hdadhh21uh1283hashdhuhh2hd
        # data:
        #     username: admin
        #     password: 123456
        #
        # <class 'str'>

        print(yaml.safe_load(stream=re), type(yaml.safe_load(stream=re)))
        #  {'method': 'get', 'url': 'http://www.baidu.com', 'headers': {'Content-Type': 'application/json', 'token': 'hdadhh21uh1283hashdhuhh2hd'}, 'data': {'username': 'admin', 'password': 123456}} <class 'dict'>
        # 返回字典格式的数据---反序列化
        return yaml.safe_load(stream=re)


if __name__ == '__main__':
    print(yaml_template({'token': 'hdadhh21uh1283hashdhuhh2hd', 'username': 'admin', 'password': '123456'}))






