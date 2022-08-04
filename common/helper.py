# _*_ coding:utf-8 _*_

import random


def gen_phonenun():
    '''自动生成手机号码'''
    phone = '1' + random.choice(['3','4','5,','7','8','9'])
    for i in range(9):
        num = random.randint(0,9)
        phone += str(num)
    return phone
