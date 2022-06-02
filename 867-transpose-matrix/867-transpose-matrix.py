class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # a new matrix with flipped dimentions
        transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for row in range(rows):
            for col in range(cols):
                # flip element dimentions 
                transpose_matrix[col][row] = matrix[row][col]
        
        return transpose_matrix