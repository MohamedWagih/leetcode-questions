class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squares = [0 for _ in range(len(nums))]
        curr_idx = n-1
        
        left, right = 0, n-1
        
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                squares[curr_idx] = nums[left]**2
                left += 1
            else:
                squares[curr_idx] = nums[right]**2
                right -= 1
            
            curr_idx -= 1
            
        return squares