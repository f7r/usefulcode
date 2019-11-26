# =============================================================================
# Author: falseuser
# Created Time: 2019-11-11 17:27:45
# Last modified: 2019-11-11 18:29:31
# Description: kruskal.py
# =============================================================================
from collections import UserDict


class DisjointSet(UserDict):
    """不相交集"""

    def add(self, item):
        self.data[item] = item

    def find(self, item):
        if self.data[item] != item:
            self.data[item] = self.find(self.data[item])
        return self.data[item]

    def union(self, item1, item2):
        self.data[item2] = self.data[item1]


def kruskal(vertexs, edges):
    # 用不相交集来判断路径是否有环路
    forest = DisjointSet()
    MST = []
    for v in vertexs:
        forest.add(v)
    edges = sorted(edges, key=lambda element: element[2])
    for e in edges:
        v1, v2, _ = e
        p1 = forest.find(v1)
        p2 = forest.find(v2)
        if p1 != p2:
            MST.append(e)
            if len(MST) == len(vertexs) - 1:
                break
            else:
                forest.union(p1, p2)
        else:
            # 表示v1,v2 都有一条可以重合路径到达p1，如果v1，v2相连，则就有环路
            print(v1, v2, p1)

    return MST


if __name__ == "__main__":
    # 无向图
    vertexs = {"A", "B", "C", "D", "E", "F", "G"}
    edges = [
        ("A", "B", 7),
        ("B", "C", 8),
        ("C", "E", 5),
        ("E", "G", 9),
        ("G", "F", 11),
        ("F", "D", 6),
        ("D", "A", 5),
        ("B", "D", 9),
        ("B", "E", 7),
        ("D", "E", 15),
        ("E", "F", 8),
    ]
    print(kruskal(vertexs, edges))
