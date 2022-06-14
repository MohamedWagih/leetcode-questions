from collections import defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        
        def lcs(w1, w2, m, n):
            if m==0 or n==0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            
            if w1[m-1] == w2[n-1]:
                dp[m][n] = 1 + lcs(w1, w2, m-1, n-1)
            else:
                dp[m][n] = max(lcs(w1, w2, m-1, n), lcs(w1, w2, m, n-1))
            
            return dp[m][n]
        
        
        return m + n - 2*lcs(word1, word2, m, n)    