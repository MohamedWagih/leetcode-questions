from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for num in freq:
            res += freq[num] * (freq[num] - 1) // 2
        return res
        