# _*_ coding:utf-8 _*_

import pymysql
from pymysql.cursors import DictCursor



class MysqlUtil:

    def __init__(self,dbconf):
        self.dbconf = dbconf
        self.conn = self.get_conn()  # 连接对象
        self.cursor = self.get_cursor()  # 游标对象

    def get_conn(self):
        """ 获取连接对象 """
        conn = pymysql.connect(host=self.dbconf['host'],
                               port=self.dbconf['port'],
                               user=self.dbconf['user'],
                               passwd=self.dbconf['pwd'],
                               db=self.dbconf['dbname'],
                               charset='utf8')
        return conn

    def get_cursor(self):
        """获取游标对象"""
        # cursor = None
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return cursor

    def query(self, sql, args=None, one=True):
        '''查询语句，默认只查询一条'''
        try:
            # 执行sql语句
            self.cursor.execute(sql, args)
            # 提交事务（使得每次游标都在初始位置）
            self.conn.commit()
            # 获取结果
            if one:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()

        except:
            # 若出现错误，则回滚
            self.conn.rollback()


    def commit_data(self, sql):
        """
        提交数据(更新、插入、删除操作)
        """
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交事务
            self.conn.commit()
        except:
            # 若出现错误，则回滚
            self.conn.rollback()


    def close(self):
        self.cursor.close()
        self.conn.close()

