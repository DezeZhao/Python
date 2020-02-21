# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 15:43
# @Software: PyCharm
# @File    : PriorityQueue.py
# @Author  : DezeZhao
# 基于list实现优先队列
class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)  # reverse=true降序，反之升序

    def is_empty(self):
        return not self._elems

    # 得到队首元素
    def peek(self):
        if self.is_empty():
            raise
        return self._elems[0]

    # 并不是在队尾插入元素  而是根据从大到小的方式插入
    def enqueue(self, e):
        i = len(self._elems) - 1  # i=0
        while i >= 0:  # i<len(self._elems)
            if self._elems[i] <= e:  # self._elems[i] >= e
                i -= 1  # i+=1
            else:
                break
        self._elems.insert(i + 1, e)  # i,e

    # 队尾元素出
    def dequeue(self):
        if self.is_empty():
            raise
        return self._elems.pop()  # list.pop()函数将最后一个元素pop


pq = PrioQue()
el = [4, 5, 2, 8, 7]
for j in el:
    pq.enqueue(j)
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
print(pq.peek())  # 得到队首元素

# 基于heap实现优先队列
