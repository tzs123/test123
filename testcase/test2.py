#coding:utf-8
import json


from common.request import HTTPHandle
from common.yanl_handler import YamlHandler

class TestApi:
    def test_api(self):
        aa = YamlHandler('../config/aaa.yaml').read_yaml()
        cc = YamlHandler('../config/bbb.yaml').read_yaml()
        req = HTTPHandle().visit(method=aa['name']['method'],
                                           url=aa['name']['url'],
                                           headers={'Accept':aa['name']['headers']['Accept'],
                                                    'Connection':aa['name']['headers']['Connection'],
                                                    'Authorization':cc['request']['token']},
                                           data=aa['name']['params'])
        ress = json.loads(req.text)
        print(ress)
    def test_api1(self):
        aa = YamlHandler('../config/aaa.yaml').read_yaml()
        cc = YamlHandler('../config/bbb.yaml').read_yaml()
        req = HTTPHandle().visit(method=aa['name2']['method'],
                                           url=aa['name2']['url'],
                                           headers={'Accept':aa['name2']['headers']['Accept'],
                                                    'Connection':aa['name2']['headers']['Connection'],
                                                    'Authorization':cc['request']['token']},
                                           data=aa['name2']['params'])
        ress = json.loads(req.text)
        print(ress)
    def test_api2(self):
        aa = YamlHandler('../config/aaa.yaml').read_yaml()
        cc = YamlHandler('../config/bbb.yaml').read_yaml()
        req = HTTPHandle().visit(method=aa['name3']['method'],
                                           url=aa['name3']['url'],
                                           headers={'Accept':aa['name3']['headers']['Accept'],
                                                    'Connection':aa['name3']['headers']['Connection'],
                                                    'Authorization':cc['request']['token']},
                                           data=aa['name3']['params'])
        ress = json.loads(req.text)
        print(ress)
