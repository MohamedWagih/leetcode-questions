class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = 0
        win_sum = 0
        win_start = 0
        for win_end in range(n):
            win_sum += nums[win_end]
            if win_end  == k - 1:
                max_sum = win_sum
                win_sum -= nums[win_start]
                win_start += 1
            elif win_end > k - 1:
                max_sum = max(max_sum, win_sum)
                win_sum -= nums[win_start]
                win_start += 1
        return max_sum / k