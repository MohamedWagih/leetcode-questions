class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(curr, path):
            if curr == len(graph)-1:
                paths.append(path)
            for adj in graph[curr]:
                dfs(adj, path+[adj])
        paths=[]
        dfs(0, [0])
        return paths
        
        