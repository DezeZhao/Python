# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 13:52
# @Software: PyCharm
# @File    : LinearList.py
# @Author  : DezeZhao


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# llist1 = LNode(1)
# p = llist1
# for i in range(2, 11):
#     p.next = LNode(i)
#     p = p.next
#
# p = llist1
# while p:
#     print(p.elem)
#     p = p.next


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return not self._head

    '''
    add a node at head
    '''

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    '''
    delete a node at head
    '''

    def pop(self):
        # if self._head is None:
        #     raise
        e = self._head.elem
        self._head = self._head.next
        return e

    '''
    delete a node at tail
    '''

    def pop_last(self):
        if not self._head:  # 表中没有元素
            raise
        p = self._head  # 表中只有一个元素
        if not p.next:
            e = p.elem
            self._head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    '''
    add a node at tail
    '''

    def append(self, elem):
        if not self._head:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                return p.elem
        p = p.next

    def traverse(self):
        p = self._head
        while p:
            print(p.elem)
            p = p.next


mlist = LList()
for i in range(1, 11):
    mlist.prepend(i)

for i in range(11, 20):
    mlist.append(i)

mlist.traverse()