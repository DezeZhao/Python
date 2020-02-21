# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 21:00
# @Software: PyCharm
# @File    : fdpcluster.py
# @Author  : DezeZhao

from graphviz import Graph

g = Graph('G', filename='fdpclust.gv', engine='fdp')

g.node('e')

with g.subgraph(name='clusterA') as a:
    a.edge('a', 'b')
    with a.subgraph(name='clusterC') as c:
        c.edge('C', 'D')

with g.subgraph(name='clusterB') as b:
    b.edge('d', 'f')

g.edge('d', 'D')
g.edge('e', 'clusterB')
g.edge('clusterC', 'clusterB')

g.view()
