from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def DFS(self):
        V = len(self.graph)
        visited = [False] * (V)
        for i in range(V):
            if not visited[i]:
                self.dfs_util(i, visited)
