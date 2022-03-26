def get_value(pos, rows, cols, mat):
    row = pos//cols
    col = pos%cols
    return mat[row][col]

class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        low = 0
        high = (rows * cols) - 1
        
        while low <= high:
            mid = (high + low) // 2 
            mid_val = get_value(mid, rows, cols, matrix)
            
            if mid_val == target:
                return True
            
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False