from collections import defaultdict
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n        
        queue = deque([0])
        while queue:
            curr_room = queue.popleft()
            if not visited[curr_room]:
                visited[curr_room] = True
                for adj_room in rooms[curr_room]:
                    queue.append(adj_room)
        
        return sum(visited ) == n
