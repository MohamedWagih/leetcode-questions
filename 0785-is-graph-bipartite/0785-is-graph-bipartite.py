class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = {}
        
        def paint(i, color):
            if i in seen:
                return seen[i] == color

            seen[i] = color
            for n in graph[i]:
                if paint(n, -color) == False:
                    return False    
            return True
            
        for i in range(len(graph)):
            if i not in seen:
                if paint(i,1) == False:
                    return False
        return True