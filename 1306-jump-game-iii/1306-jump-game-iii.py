from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = [False] * len(arr)
        while queue:
            curr = queue.popleft()
            if 0 <= curr < len(arr) and not visited[curr]:
                visited[curr]=True
                if arr[curr] == 0:
                    return True
                queue.append(curr+arr[curr])
                queue.append(curr-arr[curr])  
        return False