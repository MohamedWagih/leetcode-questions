from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # key=column number , value=set of values appeared in this column
        rows = defaultdict(set) # key=row number , value=set of values appeared in this row
        # we have 3 boxes in row (0..2) and 3 in column (0..2)
        boxes = defaultdict(set) # key=box coordinates ex:(0,1) , value=set of values appeared in this box
        
        # time complixty: O(9^2)
        for row in range(9):
            for col in range(9):
                curr_val = board[row][col]
                if curr_val == ".":
                    continue
                if (curr_val in cols[col] or curr_val in rows[row] or curr_val in boxes[(row//3, col//3)]):
                    return False
                
                cols[col].add(curr_val)
                rows[row].add(curr_val)
                boxes[(row//3, col//3)].add(curr_val)
        
        return True