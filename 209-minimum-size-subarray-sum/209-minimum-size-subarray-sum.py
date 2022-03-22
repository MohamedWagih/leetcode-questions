class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        minLength = float('inf')
        winStart = 0
        for winEnd in range(len(nums)):
            currSum += nums[winEnd]
            while currSum >= target:
                minLength = min(minLength, winEnd-winStart+1)
                currSum -= nums[winStart]
                winStart += 1
        
        if minLength == float('inf'): 
            return 0
        return minLength