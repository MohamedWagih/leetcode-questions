class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for k in freq:
            if freq[k] > 1:
                return True
        
        return False