class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            ones += n&1
            n >>= 1
        
        return ones