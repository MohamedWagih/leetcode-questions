class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev = [1] * n
        next = [1] * n
        
        for i in range(1, n):
            prev[i] = prev[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            next[i] = next[i+1] * nums[i+1]
        
        res = [1] * n
        for i in range(n):
            res[i] = prev[i] * next[i]
        
        return res