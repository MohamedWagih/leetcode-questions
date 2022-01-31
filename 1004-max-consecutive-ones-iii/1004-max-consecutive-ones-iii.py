class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        win_start, win_ones_count, max_cons_ones= 0,0,0
        
        for win_end in range(len(nums)):
            if nums[win_end] == 1:
                win_ones_count += 1
            
            num_of_zeros = win_end - win_start + 1 - win_ones_count
            if num_of_zeros > k:
                if nums[win_start] == 1:
                    win_ones_count -= 1
                win_start += 1
            max_cons_ones = max(max_cons_ones, win_end - win_start + 1)
        
        return max_cons_ones