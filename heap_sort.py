#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename:heap_sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
'''
大根堆：在一棵完全二叉树中，对于任意节点，满足性质arr[i]>=arr[2*i], arr[i]>=arr[2*i+1]
小根堆：在一棵完全二叉树中，对于任意节点，满足性质arr[i]<=arr[2*i], arr[i]<=arr[2*i+1]
'''
import randata
'''
假定除了start位置的顶点外，以start位置为root的这棵二叉树是一个大根堆
向下调整start位置的节点至合适的位置，是的这棵树重新恢复为一个大根堆
'''
def adjust(arr,start,size):
    tmp=arr[start]
    j=2*start+1
    while j<size:
        if j<size-1 and arr[j]<arr[j+1]:
            j+=1
        if tmp>=arr[j]:
            break
        arr[start]=arr[j]
        start=j
        j=2*j+1
    arr[start]=tmp
'''
从一堆乱序的元素列表中建立大根堆
'''
def buildHeap(arr):
    size=len(arr)
    for i in range(size/2-1,-1,-1):
        adjust(arr,i,size)
def heapSort(arr):
    size=len(arr)
    buildHeap(arr)
    '''
    建立大根堆后，第一个元素为列表的最大元素，将它跟最后一个元素交换，列表大小-1
    重新调整列表为大根堆，重复此操作直到最后一个元素
    '''
    for i in range(size-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        adjust(arr,0,i)
