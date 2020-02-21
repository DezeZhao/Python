# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 14:47
# @Software: PyCharm
# @File    : Stack-Queue.py
# @Author  : DezeZhao


# 顺序栈
class SStack:
    def __init__(self):
        self._elems = []

    def id_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise
        return self._elems.pop()


st1 = SStack()
st1.push(3)
st1.push(5)
print(st1.top())
st1.pop()
print(st1.top())
# 顺序队列
# class SQueue:
#     def __init__(self, init_len=9):
#         self._len = init_len
#         self._elems = [0] * init_len
#         self._head = 0  # 表头元素下标
#         self._num = 0  # 元素个数
#
#     def is_empty(self):
#         return self._num == 0
#
#     def peek(self):
#         if self._num == 0:
#             raise
#         return self._elems[self._head]
#
#     def dequeue(self):
#         if self._num == 0:
#             raise
#         e = self._elems[self._head]
#         self._head = (self._head + 1) % self._len
#         self._num -= 1
#
#     def enqueue(self, elem):
#         if self._num == self._len:
#             self.__extend()
#         self._elems[(self._head + self._num) % self._len] = elem
#         self._num += 1
#
#     def __extend(self):
#         old_len = self._len  # 0-8
#         self._len *= 2  # 18
#         new_elems = [0] * self._len  # 声明list的长度
#         for i in range(old_len):
#             new_elems[i] = self._elems[(self._head + i) % old_len]  # new_elems[0:8]存放原先的9个元素
#         self._elems, self._head = new_elems, 0
#
#
# sq1 = SQueue()
# for i in range(9):
#     sq1.enqueue(i)
# sq1.enqueue(3)
# # sq1.dequeue()
# print(sq1.peek())
