#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename:bubble_sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
#经典算法之冒泡排序（Bubble sort）

import randata
'''
算法思想：每次从最后开始往前滚，邻接元素两两相比，小元素交换到前面
第一轮循环把最小的元素上浮至第一个位置，第二小的元素上浮至第二个位置，依次类推
'''
def bubbleSort(a):
    l=len(a)-2
    i=0
    while i<=l:
        j=l
        while j>=i:
            if(a[j+1]<a[j]):
                a[j],a[j+1]=a[j+1],a[j]
            j-=1
        i+=1
