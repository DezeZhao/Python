# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 15:25
# @Software: PyCharm
# @File    : YEN_KSP.py
# @Author  : DezeZhao


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


# 顺序栈
class SStack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if not self._elems:
            raise
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if not self._elems:
            raise
        return self._elems.pop()


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


def edge2dict(A):
    B = dict()
    for path in A:
        for i in range(len(path) - 1):
            from_ = path[i]  # key
            to_ = path[i + 1]  # value
            B.setdefault(from_, set())  # 将value存放在set中去除重边
            B[from_].add(to_)
    return B


def Yen_KSP(graph, src, dest, K):  # k=1
    A = []  # 已经找到的最短路径表
    weight, path = Dijkstra(graph, src, dest)
    A.append(path)
    # A[0]=[1,3,4,6]
    # rootPath=[1] spurNode=1
    # rootPath=[1,3] spurNode=3
    # rootPath=[1,3,4] spurNode=4
    # 分别讨论上述情况下的spurPath
    # for i in range(k):
    # for k in range(len(A) - 1):  # 已经选出的k条最短路径
    candPaths = set()  # 候选路径表candidates paths 不能有重复路径，故用set
    candPath = list()
    spurPath = list()
    while len(A) < K:  # 少于K条最短路径或者候选路径集不为空
        k = len(A)
        for i in range(1, len(A[k - 1][:])):
            spurNode = A[k - 1][i - 1]  # 1
            rootPath = A[k - 1][0:i]  # 1
            rpWeight = 0
            for j in range(len(rootPath[:-1])):
                vi = rootPath[j]
                vj = rootPath[j + 1]
                if len(rootPath) == 1:
                    rpWeight += graph.get_weight(vi, vi)  # =0
                else:
                    rpWeight += graph.get_weight(vi, vj)
            edge = edge2dict(A)
            cp_graph = Graph(graph.vex_num(), graph.arc_num(), graph.copy_graph())

            for j in range(len(edge[spurNode])):
                vi = spurNode
                vj = list(edge[spurNode])[j]
                cp_graph.remove_edge(vi, vj)  # 去除不能用的边
            for j in range(len(rootPath[:-1])):
                cp_graph.remove_vex(rootPath[j])  # 去除rootPath中的不能用的节点（除了偏离节点spurNode）
            spWeight, spurPath = Dijkstra(cp_graph, spurNode, dest)
            if spWeight != float('inf'):  # 存在偏离路径，则加入候选路径集中
                candPath = rootPath[:-1] + spurPath
                weight = rpWeight + spWeight
                pathstr = ''
                for ch in candPath:
                    pathstr += str(ch)  # list不能做键，故转换为str
                candPaths.add((pathstr, weight))  # 去除重复路径，以元组的形式加入元组
        # nthShortestPath = list(candPaths)
        # nthShortestPath.sort(key=lambda x: x[1])  # set转换成list再按照weight排序
        # 或者下面的方法直接用sorted排序set[按照weight]
        candPaths = sorted(candPaths, key=lambda x: (x[1], len(x[0])))  # 得到的是列表list
        nthShortestPath = [int(ch) for ch in candPaths[0][0]]  # 恢复list
        nthShortestDist = candPaths[0][1]
        if nthShortestPath not in A:  # 最短候选路径
            A.append(list(nthShortestPath))  # 最短候选路径加入结果集A中
        candPaths.pop(0)  # 在候选路径表中删除第0项即最短路径
        candPaths = set(candPaths)  # list再转换为set
        if not candPaths:
            break
    return A  # 返回前K条最短路径


# 递归输出最短路径
def PrintShortestPath(src, dest, prev, v):
    print(src, dest)
    if src == dest:
        print(src, end="-->")
        return
    PrintShortestPath(src, prev[dest], prev, v)
    if dest == v:
        print(dest, end="")
    else:
        print(dest, end="-->")


def main():
    vexnum, arcnum, src, dest = [int(i) for i in input().strip().split()]
    arcs = [([0] * (vexnum + 1)) for _ in range(vexnum + 1)]
    graph = Graph(vexnum, arcnum, arcs)
    graph.CreateGraph()
    ksp = Yen_KSP(graph, src, dest, 8)
    print(ksp)
    # sp = Dijkstra(graph, src, dest)

    # if sp[0] == float('inf'):
    #     print("两点不连通！")
    # else:
    #     print(sp[0], sp[1])
    #     # PrintShortestPath(src, dest, sp[1], dest)


if __name__ == '__main__':
    main()
# 5 7 2 4
# 1 2 2
# 2 3 2
# 2 4 1
# 1 3 5
# 3 4 3
# 1 4 4
# 4 5 1

# 6 9 1 6
# 1 2 3
# 1 3 2
# 2 4 4
# 3 2 1
# 3 4 2
# 3 5 3
# 4 5 2
# 4 6 1
# 5 6 2

# 5 [0, 1, 1, 1, 3, 3, 4]
# 1 6
# 1 4
# 1 3
# 1 1
# 1-->3-->4-->6
