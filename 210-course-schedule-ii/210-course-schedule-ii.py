from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        # 0: not visited
        # 1: currently visiting
        # 2: visited
        visted = [0] * numCourses
        stack = []
        has_cycle = False
        
        def dfs(node):
            nonlocal has_cycle
            
            if visted[node] == 0:
                visted[node] = 1
                for adj in adj_list[node]:
                    dfs(adj)
                stack.append(node)
                visted[node] = 2
            
            # a cycle exist 
            elif visted[node] == 1:
                has_cycle = True
                return
            

        for node in range(numCourses):
            dfs(node)

        return stack[::-1] if not has_cycle else []