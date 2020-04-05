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


# 删除指定行
# 并重新写入删选后的数据到csv
import pandas as pd

data = pd.read_csv('b1.csv')
# print(data['车次']) # 输出某一列值
for item in data['车次']:
    if 'G' not in item:
        # print(data[data['车次'].isin([item])].index)
        data.drop(data[data['车次'].isin([item])].index,inplace=True)
        # 这里的inplace表示再排序的时候是否生成一个新的dataframe 结构
        # drop()方法如果不设置参数inplace=True，则只能在生成的新数据
        # 块中实现删除效果，而不能删除原有数据块的相应行。
        # df1 = df.drop([0]) #删除第0行，inplace=True则原数据发生改变
        # df1 = df.drop(cols,axis=1) # 删除指定列此处cols为[]list
        # df = df[df['身高'].isin([160])] # 选取出身高等于160 的行
        # df = df[~df['身高'].isin([160])] #取反，得到身高不等于160的行
data_ = open('./b1_update.csv','w', newline='')
df = pd.DataFrame(data) # 将列表数据data转换为DataFrame格式
df.to_csv(data_,index=False,encoding="utf-8")
#转换后的数据写入data_ csv文件  encoding 防止Excel打开乱码
# 防止读取和写入多空行 在open方法中添加关键字参数newline = ''