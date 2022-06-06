class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # no two queens can be in the same column so we keep track of visited columns
        visited_cols = set()
        # no two queens can be in the same positive diagonal so we keep track of visited positive diagonals
        # positive diagonal can be calculated as ( row - col )
        visited_diagonal_pos = set()
        # no two queens can be in the same negative diagonal so we keep track of visited negative diagonals
        # positive diagonal can be calculated as ( row + col )
        visited_diagonal_neg = set()
        
        
        def backtrack(row):
            if row == n:
                return 1
            
            solutions_count = 0
            
            for col in range(n):
                diag_pos = row + col
                diag_neg = row - col
                if not (col in visited_cols or diag_pos in visited_diagonal_pos or diag_neg in visited_diagonal_neg):
                    visited_cols.add(col)
                    visited_diagonal_pos.add(diag_pos)
                    visited_diagonal_neg.add(diag_neg)
                    
                    solutions_count += backtrack(row+1)
                    
                    visited_cols.remove(col)
                    visited_diagonal_pos.remove(diag_pos)
                    visited_diagonal_neg.remove(diag_neg)
            
            return solutions_count
                    
        return backtrack(0)