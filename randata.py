#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename:randata.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
import random
'''
随机生成0~10000000之间的数值
'''
def getrandata(num):
    a=[]
    i=0
    while i<num:
        a.append(random.randint(0,10000000))
        i+=1
    return a
