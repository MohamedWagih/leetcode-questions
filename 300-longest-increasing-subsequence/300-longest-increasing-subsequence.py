class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n
        
        # time: O(n^2)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1+ LIS[j])
        
        return max(LIS)