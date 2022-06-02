class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        transpose_matrix = []
        
        for i in range(rows):
            for j in range(cols):
                if j >= len(transpose_matrix):
                    transpose_matrix.append([])
                if i >= len(transpose_matrix[j]):
                    transpose_matrix[j].append(0)
                transpose_matrix[j][i] = matrix[i][j]
        
        return transpose_matrix