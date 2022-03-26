class Solution:
    # O(m log n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0 or cols == 0:
            return False

        # O(m) => m=rows
        for row in matrix:
            # O(log n) => n=cols
            if row[0] <= target <= row[cols-1]:
                low = 0
                high = cols-1
                while low <= high:
                    mid = (high-low)//2 + low
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
        return False
        
        