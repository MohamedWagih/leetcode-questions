class Solution:
    # Cyclic Sort
    # place every number at its correct index 
    # then looping through the array the first one isn't in place is the smallest missing
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        if n ==0:
            return 1
        
        while i < n:
            j = nums[i] -1
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] -1 != i:
                return i+1
        
        return nums[-1]+1