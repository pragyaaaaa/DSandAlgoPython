from _collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (len(self.graph))
        queue = [s]
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


# driver code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfs(2)
