class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return result
        
        currRange = []
        for i in range(len(nums)):
            if i==0 or (i > 0 and nums[i]-1 == nums[i-1]):
                currRange.append(nums[i])
                continue
            else:
                if currRange[0] == currRange[-1]:
                    result.append(str(currRange[0]))
                else:
                    result.append(str(currRange[0]) + "->" + str(currRange[-1]))
                currRange = [nums[i]]
                
        if currRange[0] == currRange[-1]:
            result.append(str(currRange[0]))
        else:
            result.append(str(currRange[0]) + "->" + str(currRange[-1]))
            
        return result