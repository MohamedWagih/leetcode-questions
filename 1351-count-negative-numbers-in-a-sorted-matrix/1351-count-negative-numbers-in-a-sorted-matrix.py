'''
 4  3  2  -1
 3  2  1  -1
 1  1 -1  -2
-1 -1 -2  -3
'''
class Solution:
    # time: O(m*log(n))
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        last_neg = cols-1
        res = 0
        
        # time: O(m)
        for row in range(rows):
            if grid[row][0] < 0:
                res += cols
                continue
            if grid[row][cols-1] >= 0:
                continue
            
            # time: O(log(n))
            l, r = 0, last_neg
            while l <= r:
                mid = l + (r-l)//2
                if grid[row][mid] >= 0:
                    l = mid+1
                else:
                    r = mid-1
            res += (cols-l)
            last_neg = l
        
        return res