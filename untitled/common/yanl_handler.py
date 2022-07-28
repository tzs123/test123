# _*_ coding:utf-8 _*_

import yaml

class YamlHandler:
    def __init__(self,path,param=None):
        self.path = path  #文件路径
        self.param = param   #不传默认获取所有数据
    def read_yaml(self,encoding='utf-8'):
        '''读取yaml数据'''
        with open(self.path,encoding=encoding) as f:
            data = yaml.load(f.read(),Loader=yaml.FullLoader)
            if self.param == None:
                return data   #获取所有数据
            else:
                return data.get(self.param)  #获取键为param的值
    def write_yaml(self,data,encoding='utf-8'):
        '''向yaml文件写入数据'''
        with open(self.path,encoding=encoding,mode='w') as f:
            return yaml.dump(data,stream=f,allow_unicode=True)


yaml_data = YamlHandler('../config/ccc.yaml').read_yaml()
yaml_data1 = YamlHandler('../config/ddd.yaml','db_info').read_yaml()
yaml_data2 = YamlHandler('../config/ddd.yaml','apihost').read_yaml()
