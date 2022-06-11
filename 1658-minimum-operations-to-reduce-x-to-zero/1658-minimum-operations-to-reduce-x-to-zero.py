class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # inorder to find the minimum [ prefix+sufix ] equal to X
        # is the same to find the maximum subarray whose sum is [sum(nums)-X ]
        
        n = len(nums)
        target = sum(nums) - x
        curr_sum = 0
        win_start = 0
        longest = 0
        possible = False
        for win_end in range(len(nums)):
            curr_sum += nums[win_end]
            while win_start <= win_end and curr_sum > target:
                curr_sum -= nums[win_start]
                win_start += 1
            if curr_sum == target:
                possible = True
                longest = max(longest, win_end - win_start + 1)
        
        return (n-longest) if possible else -1
        