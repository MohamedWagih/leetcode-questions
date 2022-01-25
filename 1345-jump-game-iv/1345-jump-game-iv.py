from collections import deque
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        last_idx = len(arr) - 1
        positions = defaultdict(list)
        for i, num in enumerate(arr):
            positions[num].append(i)
        
        visited = [False] * len(arr)
        queue = deque([0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == last_idx:
                    return steps
                if curr > 0 and not visited[curr-1]:
                    queue.append(curr-1)
                    visited[curr-1]=True
                if curr < last_idx and not visited[curr+1]:
                    queue.append(curr+1)
                    visited[curr+1]=True
                for adj in positions[arr[curr]]:
                    if adj != curr and not visited[adj]:
                        queue.append(adj)
                        visited[adj]=True
                positions[arr[curr]].clear()
                
            steps += 1
            
