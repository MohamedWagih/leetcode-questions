class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        ordered = heights[:]
        ordered.sort()
        count = 0
        for i in range(len(ordered)):
            if ordered[i] != heights[i]:
                count += 1
        return count