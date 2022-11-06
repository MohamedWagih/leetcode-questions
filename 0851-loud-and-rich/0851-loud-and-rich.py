class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i: [] for i in range(n)}
        
        # directed graph 
        for p1, p2 in richer:
            graph[p2].append(p1)
        
        answer = [None] * n
        
        def dfs(person):
            if not answer[person]:
                answer[person] = person
                for adj in graph[person]:
                    if quiet[dfs(adj)] < quiet[answer[person]]:
                        answer[person] = dfs(adj)
            
            return answer[person]

        for person in range(n):
            dfs(person)
            
        return answer