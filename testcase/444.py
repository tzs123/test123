# _*_ coding:utf-8 _*_

import pymysql


db = pymysql.connect(host = '192.168.0.219',port =3306,db='test',user='root',passwd='123',charset='utf8')
info = db.cursor()
info.execute('select id,username from sec_custinfo')
data = info.fetchall()
ret =[]
for one in data:
    line = one[0]
    line1 = one[1]
    ret.append([line,line1])
print(ret)
#结果：[['1', '董卓'], ['2', '张坤'], ['3', '王伟']]
a=[3,2,4]
b=(a.sort())
print(b)
#结果：None
