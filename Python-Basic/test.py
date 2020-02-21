# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 12:56
# @Software: PyCharm
# @File    : new.py
# @Author  : DezeZhao

#
# def f():
#     mm=[]
#     for i in range(10):
#         mat=[]
#         for j in range(10):
#             mat.append(i * j)
#         mm.append(mat)
#     return mm
#
#
# mmm=f()
#
# for i in range(10):
#     for  j in range(10):
#         print(mmm[i][j])
# arc = [[] for i in range(0, 4)]
arc = []

# def f():
#     for k in range(0, 4):
#         # v1 = eval(input())
#         # v2 = eval(input())
#         w = eval(input())
#         arc.append(w)
#     return arc
#
#
# a = f()
# for i in range(0, 4):
#         print(a[i])


# # 输入二维数组列表

n = int(input().strip())
line = [[0] * n] * n
for i in range(n):
    line[i] = input().strip().split()  # 用空格分隔
    line[i] = [int(j) for j in line[i]]  # 转换为int型数字
print(line)


# 输入一维数组列表

num = [int(n) for n in input().strip().split()]
print(num)


# a=float('inf')
# if a > 20:
#     print(1)

# 为二位列表的指定位置赋值
# arcs = [[0] * 3] * 3  # 与下面的不同

arcs = [([0] * 3) for i in range(3)]
for k in range(0, 3):
    v = input().strip().split()
    v = [int(i) for i in v]
    i, j = v[0], v[1]
    w = v[2]
    arcs[i][j] = w
print(arcs)


# 测试某1维list已经二维list中

A = []
a1 = [1, 2, 3, 4]
a2 = [2, 3, 4, 5]
A.append(a1)
A.append(a2)
A.remove(a2)
print(A)  # [0:3]即0 1 2
a3 = [3, 4]
if a3[0] in A[0][:]:
    print("[1 2 3 4]已经在A中！")



# 对列表的第二个元素排序,对set排序，可转为list用sort排序或者直接用sorted排序

li = set()
li = {('b', 6), ('a', 1), ('c', 3), ('d', 4)}
li2 = sorted(li, key=lambda x: x[1])
print(li2)
li1 = list(li)
li1.sort(key=lambda x: x[1])
print(li1)


# 对列表的第二个元素排序后，再对第一个元素排序

list=[('b',1),('a',1),('c',3),('d',4)]
list.sort(key=lambda x:(x[1],x[0]))
[('a', 1), ('b', 1), ('c', 3), ('d', 4)]


#/////////////////////////////////////////////////////////////////////
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.title('line chart')
plt.xlabel('x')
plt.ylabel('y')

plt.figure("tilesdbkvjbsdj")
plt.plot(x, y1)
plt.plot(x, y2)

plt.title('line chart')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#//////////////////////////////////////////////////////////////////////

import matplotlib.pyplot as plt
import numpy as np
# 定义数据
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
# 第一个figure
plt.figure()
plt.plot(x, y1)
# 第二个figure
plt.figure(num=3, figsize=(8, 5),)  # 尺寸(8,5)
# 第二个figure包含两个函数的显示
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # 虚线
# 显示图像
plt.show()

