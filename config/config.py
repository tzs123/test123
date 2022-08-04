# _*_ coding:utf-8 _*_

import configparser
import os

'''
    # 读取配置文件 常用的方法介绍
    cf.read(filename)    # 读取文件，返回filename的list
    cf.sections()    # 获取配置文件中所有sections的list
    cf.options(section)    # 获取指定section的键值list
    cf.items(section)    # 获取指定section下所有的键值对list
    cf.get(section, key)    # 获取指定section下指定key的value值， 返回str
    cf.getint(section, key)    # 获取指定sections下指定key的value值， 返回int
    cf.getfloat(section, key)    # 获取指定sections下指定key的value值， 返回float
    cf.getboolean(section, key)    # 获取指定sections下指定key的value值， 返回boolean
    cf.has_section(section)    # 获取是否包含某个section，返回boolean
    cf.has_option(section，key)    # 获取是否包含某个section的某个键，返回boolean
'''
# 读取配置文件
def read_config():
    root_dir = os.path.dirname(os.path.dirname(__file__))  # # 获取当前文件所在目录
    config_dir = os.path.join(root_dir, 'config', 'config.ini')  # 组装config.ini路径，也可以直接写配置文件的具体路径，不用自动获取
    cf = configparser.ConfigParser()
    cf.read(config_dir, encoding="utf-8")  # 读取config.ini
    return cf


if __name__ == '__main__':
    cf = read_config()
    host = cf.get('db_info', 'host')
    port = cf.getint('db_info', 'port') # 注意端口要用getint方法获取
    print(host)
    print(port)

