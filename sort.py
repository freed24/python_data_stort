#-*- coding: utf-8 -*-
#!/usr/bin/python
#Filename:sort.py
#Author: Boyce
#Email:  boyce.ywr@gmail.com
import time
import randata
import bubble_sort
import quick_sort
import heap_sort
import shell_sort
import merge_sort
import insert_sort
fileName='sort.dat'
size=10000
print '/nStart generate randam data...'
arr=randata.getrandata(size)
print 'Data generation finished.'
print 'Data size is %d, result will be save to file %s'%(size,fileName)
f=file(fileName,'w')
f.write("/nOriginal data:/n")
f.write(str(arr))
#使用python内置的timSort排序算法
a=arr[:]
print '/nStart internal sort...'
t1=time.clock()
a.sort()
t2=time.clock()
print 'Internal sort finisehd. Time used=%fs'%(t2-t1)
f.write('/n/nInternal sort [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart quick sort...'
t1=time.clock()
quick_sort.quickSort(a)
t2=time.clock()
print 'Quick sort finished. Time used=%fs'%(t2-t1)
f.write('/n/nQuick sort [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart heap sort...'
t1=time.clock()
heap_sort.heapSort(a)
t2=time.clock()
print 'Heap sort finished. Time used=%fs'%(t2-t1)
f.write('/n/nHeap sort [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart shell sort...'
t1=time.clock()
shell_sort.shellSort(a)
t2=time.clock()
print 'Shell sort finished. Time used=%fs'%(t2-t1)
f.write('/n/nShell sort [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart merge sort with new space...'
t1=time.clock()
merge_sort.mergeSortWithNewSpace(a)
t2=time.clock()
print 'Merge sort with new space finished. Time used=%fs'%(t2-t1)
f.write('/n/nMerge sort with new space [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart merge sort without new space...'
t1=time.clock()
merge_sort.mergeSortWithoutNewSpace(a)
t2=time.clock()
print 'Merge sort without new space finished. Time used=%fs'%(t2-t1)
f.write('/n/nMerge sort without new space [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart insert sort...'
t1=time.clock()
insert_sort.insertSort(a)
t2=time.clock()
print 'Insert sort finished. Time used=%fs'%(t2-t1)
f.write('/n/nInsert sort [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
a=arr[:]
print '/nStart bubble sort...'
t1=time.clock()
bubble_sort.bubbleSort(a)
t2=time.clock()
print 'Bubble sort finished. Time used=%fs'%(t2-t1)
f.write('/n/nBubble sort [Time used=%fs]/n'%(t2-t1))
f.write(str(a))
del a
f.close()
