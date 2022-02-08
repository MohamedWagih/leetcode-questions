class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        result = []
        while i < n:
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1 
        
        for i in range(n):
            if nums[i]-1 != i:
                result.append(i+1)
        return result
                