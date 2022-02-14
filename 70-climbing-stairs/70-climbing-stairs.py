class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)
            
            return memo[i]
        
        memo = {}
        return dp(n)