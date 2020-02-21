# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:15
# @Software: PyCharm
# @File    : rd_wt_xlsx_pandas.py
# @Author  : DezeZhao
import pandas as pd
from pandas import DataFrame


"""write excel"""
dict1 = {
    'index': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'data1': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'],
    'data2': ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
}
data = pd.DataFrame(dict1)
pd.ExcelWriter('xxx.xlsx')
data.to_excel('c.xlsx', index=False)


"""read excel"""
data = pd.read_excel('c.xlsx', sheet_name='Sheet1')
# data = data.head()  # 默认前5行

# 所有数据
print("---格式化数据---")
print(format(data))
print("---所有数据---")
print(data.values)
# print(type(data.values))  # <class 'numpy.ndarray'>

# 查看某一列所有的值/多列/指定列
print("---某一列数据---")
print(data[['index']].values)  # 输出'index'列数据
print(data[['index', 'data1']].values)  # 输出'index','data1'列数据

# 查看第一行的值/多行
print("---第1行数据---")
print(data.values[1:3])

# 行号列表输出
print("---行号列表---")
print(data.index.values)

# 列标题输出
print("---列标题---")
print(data.columns.values)

# pandas处理Excel数据成为字典
print("---pandas处理Excel数据成为字典---")
text = []
for i in data.index.values:  # 获取行号的索引,并对其进行遍历
    # 根据行号索引i来获取相应行的数据，并转换成字典格式
    row = data.loc[i, ['index', 'data1', 'data2']].to_dict()
    text.append(row)
print(format(text))
