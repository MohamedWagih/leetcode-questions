class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        boardSize = len(board)
        board.reverse()
        
        def getCoord(pos):
            r = (pos-1) // boardSize
            c = (pos-1) % boardSize
            if r%2 != 0:
                c = boardSize - 1 - c
            return [r,c]
        

        visited = set()
        queue = []
        queue.append([1,0])

        while queue:
            pos, steps = queue.pop(0)

            for nextPos in range(pos + 1, pos + 7):
                [r,c] = getCoord(nextPos)
                if board[r][c] != -1:
                    nextPos = board[r][c]
                if nextPos == boardSize * boardSize:
                    return steps + 1
                if nextPos not in visited:
                    visited.add(nextPos)
                    queue.append([nextPos, steps + 1])
        return -1