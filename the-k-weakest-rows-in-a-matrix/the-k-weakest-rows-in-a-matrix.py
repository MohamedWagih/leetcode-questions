class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts=[]
        for idx, row in enumerate(mat):
            counts.append([idx,sum(row)])
        
        res = sorted(counts, key=lambda el: el[0])
        res = sorted(res, key=lambda el: el[1])
        
        return [el[0] for el in res[:k]]