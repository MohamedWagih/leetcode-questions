class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        seen = set()
        
        def haveConnection(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for nei in graph[source]:
                    if haveConnection(nei, target):
                        return True
        
        for s, t in edges:
            seen = set()
            
            if s in graph and t in graph and haveConnection(s, t):
                return s, t
            
            graph[s].add(t)
            graph[t].add(s)
            
            