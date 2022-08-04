# _*_ coding:utf-8 _*_

import yaml

from common.excel import ExcelUtil


class ReadYaml:
    # def __init__(self, path, param=None):
    #     self.path = path  # 文件路径
    #     self.param = param  # 不传默认获取所有数据

    # 获取yaml文件中的数据
    def get_data(self,yaml_file,encoding='utf-8'):
        with open(yaml_file,'r',encoding=encoding) as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
            print(data)
            return data
            # if self.param == None:
            #     return data  # 返回所有数据
            # else:
            #     return data.get(self.param)  # 获取键为param的值
    #写入yaml
    def write_yaml(self,data,yaml_file,encoding='utf-8'):
        '''向yaml文件写入数据'''
        with open(yaml_file,encoding=encoding,mode='w') as f:
            yaml.dump(data,stream=f,allow_unicode=True,sort_keys=False,default_flow_style=False)

    #清除yaml
    def truncate_yaml(self,yaml_file):
        with open(yaml_file, mode='w') as f:
            f.truncate()

    def handler(self):
        '''
        根据读取excel数据，生成yaml测试用例数据
        :return:
        '''
        file ='%s/data/接口测试用例.xlsx'% base_dir
        value = ExcelUtil(file).read_excel()
        sheet_names = ExcelUtil(file).wb.sheetnames
        n =0
        for sheet in sheet_names:
            data = value[n]
            file = '%s/data/%s.yaml'% (base_dir,sheet)
            self.write_yaml(data=data, yaml_file=file)
            n += 1

