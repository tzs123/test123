# _*_ coding:utf-8 _*_
import jsonpath
import pymysql

from common.YamlHandler import yaml_data


class CommDB(object):
    '''构造函数，初始化数据库连接参数'''
    def __init__(self,host,port,db,user,passwd,charset):
        self.host = host
        self.port =port
        self.db = db
        self.user =user
        self.passwd = passwd
        self.charset = charset

    def execSql(self, strSql, bVerify=False):
        try:
            rc = [True, None]
            # 获取数据库连接，使用参数
            conn = pymysql.connect(host=self.host, port=self.port,
                                   user=self.user, passwd=self.passwd,
                                   db=self.db, charset=self.charset)
            cur = conn.cursor()  # 获取一个游标
            cur.execute(strSql)  # 执行一条数据库查询语句
            data = cur.fetchall()  # 将执行结果返回给data,data是一个二维元组
            # 无执行错误表示SQL执行成功
            if bVerify:  # 执行的是验证语句
                rc[0] = True  # 表示sql语句执行成功
                rc[1] = data[0][0]  # SQL语句返回的第一行第一列数据赋值给返回数组
            elif len(data) >= 1:  # 如果返回的数据大于一行，且不是执行的验证SQL
                rc[0] = True  # 表示sql语句执行成功
                rc[1] = data  # SQL语句返回全部数据，是一个二维数组
            else:  # 如果没有返回数据
                rc[0] = True  # 表示sql语句执行成功
                rc[1] = None  # 数据赋值为None
            cur.execute("commit;")  # 执行一条数据库提交语句
            # cur.execute("rollback;") #执行一条数据库回滚语句
            cur.close()
            conn.close()
        except Exception as e:
            try:
                conn.close()  # 执行一条连接关闭操作
            except Exception as ee:
                pass
            # print("发生异常：%s"%e)
            rc[0] = False  # 数据库操作失败了
            rc[1] = "发生异常：%s" % e  # 错误提示信息是什么
        return rc
sql =CommDB(host=yaml_data['mysql']['host'],user=yaml_data['mysql']['user'], passwd=yaml_data['mysql']['passwd'],
        port=yaml_data['mysql']['port'], db=yaml_data['mysql']['db'], charset=yaml_data['mysql']['charset']).execSql('select * from user')

# print(list(sql[1])[0][4])
# print(type((list(sql[1])[0][4]).split(',')))

