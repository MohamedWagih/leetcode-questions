class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for idx, n in enumerate(nums):
            for i in range(len(nums)):
                if i != idx and nums[i] < n:
                    res[idx] += 1
        return res