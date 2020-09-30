import sys


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex distance from source: ")
        for node in range(self.V):
            print(node, "t", dist[node])

    def min_distance(self, dist, spt_set):
        min_size = sys.maxsize
        for v in range(self.V):
            if dist[v] < min_size and spt_set[v] == False:
                min_size = dist[v]
                min_index = v
        return min_index

    def dijktra(self, src):
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        spt_set = [False] * self.v
        for cout in range(self.v):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and \
                        spt_set[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_solution(dist)
