class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        longest = 0
        dp = [0 for _ in range(n)]
        
        for i in range(1, n):
            
            if s[i]==')' and s[i-1]=='(':
                dp[i] = 2 + (dp[i-2] if i >=2 else 0)
            
            elif s[i]==')' and s[i-1]==')':
                if i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)
                    
            longest = max(longest, dp[i])
            
        return longest