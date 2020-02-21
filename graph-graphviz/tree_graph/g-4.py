# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 13:31
# @Software: PyCharm
# @File    : g-4.py
# @Author  : DezeZhao
from graphviz import Graph

g = Graph(name='tree', comment=None,
          filename='tree_graph.gv', directory=None,
          format='pdf', engine=None,
          encoding='utf-8',
          graph_attr={'rankdir': 'TB'},
          node_attr={'shape': 'circle'}  # edge_attr为默认
          )
g.node('0', '000')
g.node('1', '111')
g.node('2', '222')
g.node('3', '333')

# g.edge('0', '1')
# g.edge('0', '2')
a = set(['01', '02'])  # 等同于以上
b = set(['13', '14'])
c = set(['25', '26'])
d = set(['39', '3a'])
g.edges(a | b | c | d)
g.view()
