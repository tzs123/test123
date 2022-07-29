# !/usr/bin/env python
# _*_ coding:utf-8 _*_


def test1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()