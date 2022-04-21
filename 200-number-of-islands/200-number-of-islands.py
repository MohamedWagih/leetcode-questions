from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        visited = set()
        
        def visit(row, col, queue):
            if min(row,col) < 0 or row==m or col==n:
                return
            if grid[row][col] == "1":
                queue.append((row, col))
                grid[row][col] = "2"
                
        
        def bfs(row, col):
            queue = deque()
            queue.append((row,col))
            grid[row][col] = "2"
            while queue:
                x = len(queue)
                for _ in range(x):
                    curr_row, curr_col = queue.popleft()
                    visit(curr_row+1, curr_col, queue)
                    visit(curr_row-1, curr_col, queue)
                    visit(curr_row, curr_col+1, queue)
                    visit(curr_row, curr_col-1, queue)

        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    bfs(row,col)
                    count += 1
        
        return count