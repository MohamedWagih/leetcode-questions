class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return result
        
        start, end = 0,0
        while end < len(nums):
            while end+1 < len(nums) and nums[end]+1 == nums[end+1]:
                end += 1
            
            if start == end:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[end]))
            
            end += 1
            start = end
                
        return result