class Solution:
    def countPoints(self, rings: str) -> int:
        rods = dict()
        for i in range(1,len(rings),2):
            rods[int(rings[i])+1] = set()
        for i in range(1,len(rings),2):
            rods[int(rings[i])+1].add(rings[i-1])

        count = 0
        for rod in rods:
            if len(rods[rod]) == 3 :
                count += 1
        return count
        