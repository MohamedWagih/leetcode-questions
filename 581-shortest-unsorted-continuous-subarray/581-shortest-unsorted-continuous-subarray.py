class Solution:
    # O(n)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        # find first unsorted item form left
        while low < len(nums) -1 and nums[low] <= nums[low+1]:
            low += 1
        
        # return 0 if array is already sorted
        if low == len(nums) -1 :
            return 0
        
        # find first unsorted item from right
        while high > 0 and nums[high-1] <= nums[high]:
            high -= 1
            
        subarray_min = float('inf')
        subarray_max = float('-inf')
        for k in range(low, high+1):
            subarray_min = min(subarray_min, nums[k])
            subarray_max = max(subarray_max, nums[k])
        
        # extend subarray from left to include any item less than min item in subarray
        while low > 0 and nums[low-1] > subarray_min :
            low -= 1
            
        # extend subarray from right to include any item less tnan max item in subarray
        while high < len(nums)-1 and nums[high+1] < subarray_max:
            high += 1
        
        return high - low + 1 
        