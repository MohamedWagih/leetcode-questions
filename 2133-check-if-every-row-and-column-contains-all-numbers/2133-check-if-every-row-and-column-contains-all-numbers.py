from collections import defaultdict

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        # time complixty: O(n^2)
        for row in range(n):
            for col in range(n):
                curr_num = matrix[row][col]
                rows[row].add(curr_num)
                cols[col].add(curr_num)
        
        for row in range(n):
            if len(rows[row]) != n:
                return False
            
        for col in range(n):
            if len(cols[col]) != n:
                return False
        
        return True
            