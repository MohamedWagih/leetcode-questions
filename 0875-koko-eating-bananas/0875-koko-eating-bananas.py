class Solution:
    def canFinishEating(self, piles, speed, hoursLimit):
        needed = 0
        for p in piles:
            needed += ( (p-1) // speed ) + 1
        return needed <= hoursLimit

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + ( right - left) // 2
            
            if self.canFinishEating(piles[:], mid, h):
                right = mid
            
            else: 
                left = mid + 1
            
        return left