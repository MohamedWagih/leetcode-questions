from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    queue.append([x,y])
        
        if len(queue) == 0 and fresh == 0:
            return 0
        
        visited = set()
        minutes = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_x, curr_y = queue.popleft()
                for x, y in [[curr_x, curr_y-1], [curr_x, curr_y+1], [curr_x-1, curr_y], [curr_x+1, curr_y]]:
                    if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                        if grid[x][y] == 1:
                            queue.append([x, y])
                            visited.add((x,y))
            minutes += 1
        
        if len(visited) != fresh:
            return -1
        
        return minutes-1