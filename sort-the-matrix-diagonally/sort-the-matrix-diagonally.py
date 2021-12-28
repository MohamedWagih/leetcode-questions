import heapq
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        heap = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                heapq.heappush(heap, [i-j, mat[i][j],i,j])

        dic = {}
        while heap:
            el = heapq.heappop(heap)
            diag = el[0]
            val = el[1]
            i = el[2]
            j = el[3]
            mat[i-min(i,j) + dic.get(diag,0)][j-min(i,j)+ dic.get(diag,0)] = val
            dic[diag] = dic.get(diag,0) + 1
        
        return mat