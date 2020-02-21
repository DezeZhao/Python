# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 10:49
# @Software: PyCharm
# @File    : Dijkstra.py
# @Author  : DezeZhao


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


class Graph:
    def __init__(self, vexnum, arcnum, arcs=[]):
        self._vexnum = vexnum
        self._arcnum = arcnum
        self._arcs = arcs
        self._vexs = [vexnum + 1]

    def copy_graph(self):
        vexnum = self._vexnum
        arcnum = self._arcnum
        mat = [([0] * (vexnum + 1)) for _ in range(vexnum + 1)]
        for i in range(1, vexnum + 1):
            for j in range(1, vexnum + 1):
                mat[i][j] = self._arcs[i][j]
        return mat

    def vex_num(self):
        return self._vexnum

    def arc_num(self):
        return self._arcnum

    def get_arcs(self):
        return self._arcs

    def add_edge(self, vi, vj, w):
        self._arcs[vi][vj] = w

    def get_weight(self, vi, vj):
        return self._arcs[vi][vj]

    def remove_edge(self, vi, vj):
        self._arcs[vi][vj] = float('inf')

    def remove_vex(self, vex):
        for i in range(1, self._vexnum + 1):
            if self._arcs[vex][i] != float('inf'):
                self._arcs[vex][i] = float('inf')

    def CreateGraph(self):
        vexnum = self._vexnum
        arcnum = self._arcnum
        arcs = self._arcs
        vexs = self._vexs
        i, j, k = 0, 0, 0
        # for i in range(1, vexnum + 1):
        #     vexs[i] = i

        for i in range(1, vexnum + 1):
            for j in range(1, vexnum + 1):
                arcs[i][j] = float('inf')
                arcs[i][i] = 0

        for k in range(1, arcnum + 1):
            v = input().strip().split()
            v = [int(i) for i in v]  # 转换为数字
            i, j = v[0], v[1]
            w = v[2]
            arcs[i][j] = w


def Dijkstra(graph, v0, u0):
    vexnum = graph.vex_num()  # 图的节点数
    final = [0] * (vexnum + 1)
    D = [0] * (vexnum + 1)
    prev = [i for i in range(0, vexnum + 1)]  # 结点i的前驱结点是i
    min_, i, v = 0, 0, 0
    for v in range(1, vexnum + 1):
        D[v] = graph.get_weight(v0, v)  # 初始化最短距离
        prev[v] = v0  # 初始化前驱结点

    D[v0] = 0
    final[v0] = 1  # 初始化,v0属于S
    for i in range(2, vexnum + 1):
        min_ = float('inf')
        for w in range(1, vexnum + 1):
            if not final[w] and D[w] < min_:
                v = w
                min_ = D[w]
        final[v] = 1
        # 更新当前最短距离D[]及路径表Path[][]
        for w in range(1, vexnum + 1):
            if not final[w] and min_ + graph.get_weight(v, w) < D[w]:
                D[w] = min_ + graph.get_weight(v, w)
                # 此时D[w]的值通过结点v进行了改写,及源点到w结点的距离相比原来更小了且经过结点v
                prev[w] = v  # w结点的前驱结点是v
    # 输出最短路径
    stack = SStack()
    stack.push(u0)
    path = []
    top = stack.top()
    while prev[top] != v0:
        stack.push(prev[top])
        top = stack.top()
    path.append(v0)
    while not stack.is_empty():
        path.append(stack.pop())

    return D[u0], path
