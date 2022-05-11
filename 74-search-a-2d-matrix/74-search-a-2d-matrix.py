
class Solution:
    # time: O( log m + log m) == O( log m*n )
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        # 1) serch for the right row
        # time: O(log m)
        top, bottom = 0, rows-1
        while top <= bottom:
            mid_row = top + (bottom-top)//2
            
            if target < matrix[mid_row][0]:
                bottom = mid_row-1
            elif target > matrix[mid_row][-1]:
                top = mid_row+1
            else:
                break
                
        # if did not find a suitable row return False
        if not (top <= bottom):
            return False
        
        # 2) search for target in the suitable row we found
        # time: O(log n)
        mid_row = top + (bottom-top)//2
        left, right = 0, cols-1
        while left <= right:
            mid = left + (right-left)//2
            
            if target == matrix[mid_row][mid]:
                return True
            
            if target < matrix[mid_row][mid]:
                right = mid - 1
            elif target > matrix[mid_row][mid]:
                left = mid + 1
            
        return False
