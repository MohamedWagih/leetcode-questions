class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def isClosed(i, j):
            # base case
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            # if it's water so this direction is closed
            if grid[i][j] == 1:
                return True
            # now we are in water
            # mark as visited 
            grid[i][j] = 1
            
            # visit 4 directions
            left = isClosed(i-1, j)
            right = isClosed(i+1, j)
            up = isClosed(i, j-1)
            down = isClosed(i, j+1)
            
            # return is 4 directions is closed
            return left and right and up and down

            
            
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if isClosed(i, j):
                        islands += 1 
        return islands