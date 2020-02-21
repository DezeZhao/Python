# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 15:40
# @Software: PyCharm
# @File    : Tree.py
# @Author  : DezeZhao


# 二叉树结点类
class BinTNode:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


# 递归
def count_BinTNodes(t):
    if not t:
        return 0
    else:
        return 1 + count_BinTNodes(t.lchild) \
               + count_BinTNodes(t.rchild)


# 递归
def sum_BinTNodes(t):
    if not t:
        return 0
    else:
        return t.data + sum_BinTNodes(t.lchild) \
               + sum_BinTNodes(t.rchild)


# 递归先序遍历
def PreOrderTraverse(t):
    if not t:
        return
    print(t.data)
    PreOrderTraverse(t.lchild)
    PreOrderTraverse(t.rchild)


# 递归中序遍历
def InOrderTraverse(t):
    if not t:
        return
    InOrderTraverse(t.lchild)
    print(t.data)
    InOrderTraverse(t.rchild)


# 递归后序遍历
def PostOrderTraverse(t):
    if not t:
        return
    PostOrderTraverse(t.lchild)
    PostOrderTraverse(t.rchild)
    print(t.data)


btn = BinTNode(1,
               BinTNode(2,
                        BinTNode(4),
                        BinTNode(5)
                        ),
               BinTNode(3,
                        BinTNode(6)
                        )
               )

cnt = count_BinTNodes(btn)
sum_ = sum_BinTNodes(btn)
print(cnt, sum_)
print("先序遍历递归")
PreOrderTraverse(btn)
print("中序遍历递归")
InOrderTraverse(btn)
print("后序遍历递归")
PostOrderTraverse(btn)


# 二叉树类
class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def leftchild(self):
        return self._root.lchild

    def rightchild(self):
        return self._root.rchild

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftnode):
        self._root.lchild = leftnode

    def set_right(self, rightnode):
        self._root.rchild = rightnode
