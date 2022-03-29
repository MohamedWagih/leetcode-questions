class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        result = 0
        win_start = 0
        win_product = 1
        for win_end in range(len(nums)):
            win_product *= nums[win_end]
            while win_product >= k:
                win_product /= nums[win_start]
                win_start += 1
            
            result += win_end - win_start + 1
        
        return result