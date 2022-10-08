class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        
        for idx, num in enumerate(nums):
            candidate =  target - num
            if candidate in candidates:
                return [candidates[candidate], idx]
            candidates[num] = idx
        