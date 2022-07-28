# _*_ coding:utf-8 _*_
import pymysql


class MysqlUtil:
    def __init__(self,dbconf):
        self.dbconf = dbconf
        self.conn = self.get_conn()
        self.cursor = self.get_cursor()

    def get_conn(self):
        conn = pymysql.connect(host=self.dbconf['host'],
                               port=self.dbconf['port'],
                               user=self.dbconf['user'],
                               passwd=self.dbconf['pwd'],
                               db=self.dbconf['dbname'],
                               charset='utf8'
                               )
        return conn

    def get_cursor(self):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return cursor

    def query(self,sql,args=None,one=True):
        try:
            self.cursor.execute(sql,args)
            self.conn.commit()
            if one:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()
        except:
            self.conn.rollback()

    def commit_data(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()