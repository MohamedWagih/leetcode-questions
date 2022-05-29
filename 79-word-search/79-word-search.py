class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, curr_char_idx):
            if curr_char_idx == len(word):
                return True
            
            if (min(row,col) < 0 
                or row>=ROWS or col>=COLS
                or word[curr_char_idx] != board[row][col] 
                or (row,col) in visited):
                return False
                        
            visited.add((row, col))
            found = (dfs(row + 1, col, curr_char_idx + 1) or
                   dfs(row - 1, col, curr_char_idx + 1) or
                   dfs(row, col + 1, curr_char_idx + 1) or
                   dfs(row, col - 1, curr_char_idx + 1))
            visited.remove((row, col))
            
            return found
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False
            