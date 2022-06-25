class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if modified or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                modified = True
        
        return True