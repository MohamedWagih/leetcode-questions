class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        
        while left < right:
            mid = left + ( right - left ) // 2
            
            operations = 0
            for n in nums:
                operations += (n-1) // mid
            
            if operations > maxOperations:
                left = mid + 1
            
            else:
                right = mid 
        
        return left