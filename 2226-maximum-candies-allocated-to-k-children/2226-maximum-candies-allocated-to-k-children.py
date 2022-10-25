class Solution:
    def canBeAllocated(self,n, candies, children):
        num_of_piles = 0
        for c in candies:
            num_of_piles += c // n
        
        return num_of_piles >= children
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        
        while left < right:
            mid = left + ( right - left  + 1) // 2

            if self.canBeAllocated(mid, candies[:], k):
                left = mid             
            else:
                right =  mid - 1
            
        if self.canBeAllocated(left, candies[:], k):
            return left
        else:
            return 0
