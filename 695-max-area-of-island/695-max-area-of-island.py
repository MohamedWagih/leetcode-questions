class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0
        visited = set()
    
        def visit(row, col, queue):
            if min(row,col) < 0 or row==m or col==n:
                return 0
            
            if grid[row][col] == 1:
                queue.append((row, col))
                grid[row][col] = 2
                return 1
            else:
                return 0
        
        def bfs(row, col):
            queue = deque()
            queue.append((row,col))
            grid[row][col] = 2
            area = 1
            while queue:
                x = len(queue)
                for _ in range(x):
                    curr_row, curr_col = queue.popleft()
                    area += visit(curr_row+1, curr_col, queue)
                    area += visit(curr_row-1, curr_col, queue)
                    area += visit(curr_row, curr_col+1, queue)
                    area += visit(curr_row, curr_col-1, queue)
            return area

        max_area = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = bfs(row,col)
                    max_area = max(area, max_area)
                    
        return max_area 
