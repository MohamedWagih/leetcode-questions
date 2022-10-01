class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1,len(nums)):
            if nums[right] == nums[left]:
                continue
                
            left += 1
            nums[left] = nums[right]
        
        return left+1