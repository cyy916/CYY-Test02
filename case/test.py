# -*- coding:utf-8 -*-
'''
@ File: test.py
@ Date:2021/1/3
@ Author:chenyuanyuan
@ version：python 3.8.2
'''

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
