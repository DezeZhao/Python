# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 19:37
# @Software: PyCharm
# @File    : g-5.py
# @Author  : DezeZhao
from graphviz import Digraph, nohtml


def graph(n, ch):
    dg = Digraph('btree', engine='dot', filename='btree.gv', node_attr={'shape': 'record'})

    for i in range(0, int(n)):
        dg.node('node%d' % i, nohtml('<f0>|<f1> %c|<f2>' % (ord(ch) + i)))  # 字符转换为数字
    # dg.node('node1', nohtml('<f0>|<f1> B|<f2>'))
    # dg.node('node2', nohtml('<f0>|<f1> C|<f2>'))
    # dg.node('node3', nohtml('<f0>|<f1> D|<f2>'))
    # dg.node('node4', nohtml('<f0>|<f1> E|<f2>'))
    # dg.node('node5', nohtml('<f0>|<f1> F|<f2>'))
    # dg.node('node6', nohtml('<f0>|<f1> G|<f2>'))
    # dg.node('node7', nohtml('<f0>|<f1> H|<f2>'))
    # dg.node('node8', nohtml('<f0>|<f1> I|<f2>'))

    dg.edge('node0:f0', 'node1:f1')
    dg.edge('node0:f2', 'node2:f1')
    dg.edge('node1:f0', 'node3:f1')
    dg.edge('node1:f2', 'node4:f1')
    dg.edge('node2:f0', 'node5:f1')
    dg.edge('node2:f2', 'node6:f1')
    dg.edge('node3:f0', 'node7:f1')
    dg.edge('node3:f2', 'node8:f1')

    dg.view()


def main():
    ch = 'A'
    n = 9
    graph(n, ch)


if __name__ == '__main__':
    main()
