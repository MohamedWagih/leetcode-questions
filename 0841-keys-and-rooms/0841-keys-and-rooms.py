class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)

        queue = [0]        
        while queue:
            curr = queue.pop()
            if not visited[curr]:
                visited[curr] = 1
                for room in rooms[curr]:
                    queue.append(room)
        
        for room in range(len(rooms)):
            if not visited[room]:
                return False
        
        return True