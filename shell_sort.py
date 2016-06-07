#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename: shell_sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
# 经典算法之希尔排序（Shell sort）
# 希尔排序的名称源于它的发明者Donald Shell，该算法是冲破二次时间屏障的第一批算法之一，不过，直到它最初被发现的若干年后才被证明了它的亚二次时间界。它通过比较相距一定间隔的元素来工作；各趟比较所用的距离随着算法的进行而减小，直到只比较相邻元素的最后一趟排序为止。

import randata
def shellSort(arr):
    dist=len(arr)/2
    while dist>0:
        for i in range(dist,len(arr)):
            tmp=arr[i]
            j=i
            while j>=dist and tmp<arr[j-dist]:
                arr[j]=arr[j-dist]
                j-=dist
            arr[j]=tmp
        dist/=2
