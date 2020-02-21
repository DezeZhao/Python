# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 12:59
# @Software: PyCharm
# @File    : g-3.py
# @Author  : DezeZhao
from graphviz import Digraph

gz = Digraph(name='flowchart', filename='flowchart.gv',
             format='pdf', encoding='UTF-8')
gz.node_attr.update(fontname='NSimSun', shape='box', style='rounded')
gz.edge_attr.update(fontname='Kaiti')
gz.node('0', '会议')
gz.node('1', '直播会议')
gz.node('2', '直播页面')
gz.node('a', '现场会议')
gz.node('b', '报名')
gz.node('i', '报名')
gz.node('c', '选择门票')
gz.node('d', '填写需求单')
gz.node('j', '填写需求单')
gz.node('e', '报名成功', {'color': 'red', 'fontcolor': 'red'})
gz.node('f', '订单页面')
gz.node('g', '报名购票成功', {'color': 'red', 'fontcolor': 'red'})

t = set(['01', '0a', '12'])
a = set(['ab', 'bd', 'de'])
b = set(['ab', 'be'])
c = set(['ac', 'ci', 'ij', 'jf', 'fg'])
d = set(['ac', 'ci', 'if', 'fg'])
gz.edges(a | b | c | d | t)
gz.edge('c', 'f', '已报名')
print(gz.source)
gz.view()
