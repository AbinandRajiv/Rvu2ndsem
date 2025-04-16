class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph [u] = []
        if v not in self.graph:
            self.graph [v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
            
    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=" ") 
            visited.add(vertex)
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

graph.dfs(1)

