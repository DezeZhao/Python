# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 20:13
# @Software: PyCharm
# @File    : test.py
# @Author  : DezeZhao
import csv
import pandas as pd
import numpy as np

"""
for i in ('A', 'B'):
    print("%c" % (ord(i) + 1))
    print("dcsdkjcbsd%c:" % (ord(i) + 1), i)

c = set(['12', 'dee'])
d=set()
print(c)

a = set('abracadabra')
print(a)

list1=[]
for i in range(10):
    list1.append(i)
print(list1)

dict1={}
for j in range(10):
    dict1[j]=j
print(dict1)
"""

# 第一种方法读写csv——python IO
"""
# write
with open('a.csv', 'w', newline='') as csvfile:  # 必须要加newline=''否则会有空行
    writer = csv.writer(csvfile)
    # 先写column name
    writer.writerow(['index', 'a', 'b'])
    # 写入多行是 writerows
    list1 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    writer.writerows(list1)

# read
with open('a.csv', 'r') as csvfile1:
    reader = csv.reader(csvfile1)
    header = next(reader)
    print(header)
    print(type(reader))  # <class '_csv.reader'>
    list1 = []
    for line in reader:
        list1.append(line)

reader = [[int(x) for x in row] for row in list1]  # str转换为int
print(type(reader))  # <class 'list'>
reader = np.array(reader)
print(type(reader))  # <class 'numpy.ndarray'>
print(reader)  # np.array数组
"""

# a1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(a1.shape)  # (2,3)
# print(type(a1))
# print(a1)

"""
# 第二种方法读取csv文件——使用pandas
csv_data = pd.read_csv('a.csv')
print(csv_data.shape)  # 几行几列
csv_batch_data=csv_data.tail(2)  # 读取末尾两行数据
print(csv_batch_data.shape)  # 2,3
print(csv_data)
print(type(csv_data))  # <class 'pandas.core.frame.DataFrame'>
"""