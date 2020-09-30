import sys


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex distance from source: ")
        for node in range(self.v):
            print(node, "to", dist[node])

    def min_distance(self, dist, spt_set):
        min_size = sys.maxsize
        for v in range(self.v):
            if dist[v] < min_size and spt_set[v] == False:
                min_size = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
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


# driver code
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);
