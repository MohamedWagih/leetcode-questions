class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        
        
        for u, v in connections:
            graph[u].append([v, True])  # True indicated the road direction from U to V
            graph[v].append([u, False]) # False indicated the road direction from V to U

        
        visited = set()
        visited.add(0)
        
        return self.dfs(0, visited, graph)
        
    def dfs(self, u, visited, graph):
        result = 0
        
        for v, direction in graph[u]:
            if v not in visited:
                visited.add(v)
                result += direction
                result += self.dfs(v, visited, graph)
        
        return result
        