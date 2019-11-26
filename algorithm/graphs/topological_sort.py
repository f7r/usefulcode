# =============================================================================
# Author: falseuser
# Created Time: 2019-11-08 15:50:37
# Last modified: 2019-11-08 17:39:38
# Description: 有向无环图的拓扑排序
# =============================================================================


def sort(graph):
    sorted_list = []
    # 指向某个顶点的路径数
    counts = {k: 0 for k in graph.keys()}
    for v in graph:
        for t in graph[v]:
            counts[t] = counts[t] + 1

    from collections import deque
    Q = deque()
    # 所有没有依赖顶点的节点先放入Q
    for v in graph:
        if counts[v] == 0:
            Q.append(v)

    def sort_rec():
        if len(Q) == 0:
            return

        v = Q.popleft()

        sorted_list.append(v)
        for t in graph[v]:
            # v在Q里面则指向t的路径数减少
            counts[t] = counts[t] - 1
            if counts[t] == 0:
                Q.append(t)
        sort_rec()


    sort_rec()
    return sorted_list


if __name__ == "__main__":
    g = {
        'A': ['G'],
        'B': ['A', 'D'],
        'C': ['F', 'G'],
        'D': ['E', 'F'],
        'E': [],
        'F': [],
        'G': [],
    }
    print(sort(g))
