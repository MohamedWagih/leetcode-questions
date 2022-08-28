class Solution:
    # t: O((m+n) * k) where k=min(m,n)
    # space: O(1)
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # going diagonally from every column start
        # t: O(n)
        for col in range(0, n):
            # t: O(k) 
            self.sortDiagonal(mat, 0, col, m, n)
        
        # going diagonally form each row start
        # t: O(m)
        for row in range(1, m):
            # t: O(k)
            self.sortDiagonal(mat, row, 0, m, n)
        
        return mat
    
    # Sorting each diagonal
    # count sort
    def sortDiagonal(self, mat, row, col, m, n):
        # space: O(100) ==> O(1)
        count = [0 for _ in range(101)]
        r, c = row, col
        while r<m and c<n:
            count[mat[r][c]] += 1
            r +=1
            c +=1
        
        r, c = row, col
        for i in range(1, 101):
            while count[i] > 0:
                mat[r][c] = i
                count[i] -= 1
                r +=1
                c +=1
        