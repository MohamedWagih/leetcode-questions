class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        n=len(graph)
        paths=[]
        stack=[]
        stack.append((0,[0]))
        
        while stack:
            node, path = stack.pop()
            if node == n-1:
                paths.append(path)
                
            for adj in graph[node]:
                stack.append((adj, path+[adj]))
        
        return paths
        
        