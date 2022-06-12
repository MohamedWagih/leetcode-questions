class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        win_start = 0
        win_sum = 0
        max_score = 0
        
        for win_end in range(len(nums)):
            end_num = nums[win_end]
            while win_start <= win_end and end_num in seen:
                win_sum -= nums[win_start]
                seen.remove(nums[win_start])
                win_start += 1
            
            win_sum += end_num
            seen.add(end_num)
            max_score = max(max_score, win_sum)
        
        return max_score