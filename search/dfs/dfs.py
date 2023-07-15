from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)
    
    def _dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("DFS traversal starting from vertex 2:")
    g.dfs(2)
