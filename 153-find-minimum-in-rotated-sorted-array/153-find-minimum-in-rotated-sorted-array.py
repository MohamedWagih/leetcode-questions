class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1 :
            return nums[0]
        
        left, right = 0, n-1
        
        # if the array already sorted (not shifted) return the first element
        if nums[left] < nums[right]:
            return nums[0]
        
        while left<=right:
            mid = left + (right-left)//2
            
            # if mid is the pivot then mid+1 is the smallest element
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # if mid-1 is the pivot then mid is the smallest element
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            # if mid > start so we are in the left part (greater values) 
            # then jumb to the right part of the array ( smaller part )
            if nums[mid] > nums[0]:
                left = mid+1
            # otherwise we already in the right part ( smaller part )
            # then move left to the smallest value
            else:
                right = mid-1
