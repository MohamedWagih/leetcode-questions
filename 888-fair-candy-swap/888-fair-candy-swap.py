class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2 
        set_alice = set(aliceSizes)
        
        for b in bobSizes:
            if diff+b in set_alice:
                return [diff+b, b]