# =============================================================================
# Author: falseuser
# Created Time: 2019-11-08 14:28:32
# Last modified: 2019-11-08 15:39:41
# Description: depth_first_search.py
# =============================================================================

class Graph:
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        print(self.vertex)
        for i in self.vertex.keys():
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]
            if toVertex not in self.vertex.keys():
                self.vertex[toVertex] = []

    def DFS(self):
        # visited array for storing already visited nodes
        visited = {k: False for k in self.vertex}

        # call the recursive helper function
        for i in self.vertex.keys():
            if visited[i] == False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # mark start vertex as visited
        visited[startVertex] = True

        print(startVertex, end=" ")

        # Recur for all the vertexes that are adjacent to this node
        for i in self.vertex[startVertex]:
            if visited[i] == False:
                self.DFSRec(i, visited)

    def bfs(self):
        visited = {k: False for k in self.vertex}
        for i in self.vertex.keys():
            if visited[i] == False:
                print(i, end=" ")
                visited[i] = True
            for j in self.vertex[i]:
                if visited[j] == False:
                    print(j, end=" ")
                    visited[j] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('B', 'C')
    g.addEdge('B', 'E')
    g.addEdge('B', 'F')
    g.addEdge('C', 'E')
    g.addEdge('D', 'C')
    g.addEdge('E', 'B')
    g.addEdge('E', 'D')
    g.addEdge('F', 'G')

    g.printGraph()
    print("DFS:")
    g.DFS()
    print()
    g.bfs()
    print()
