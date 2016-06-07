#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename: insert_sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
# 经典算法之直接插入排序（Insert sort）

import randata
'''
被注释掉的部分是c语言数组普通的插入方式
未被注释的部分则是使用python列表的插入和删除特性改善的
'''
def insertSort(arr):
    for i in range(1,len(arr)):
        '''
        tmp=arr[i]
        j=i
        while j>0 and tmp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=tmp
        '''
        j=i
        while j>0 and arr[j-1]>arr[i]:
            j-=1
        arr.insert(j,arr[i])
        arr.pop(i+1)
