class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        
        envelopes.sort(key= lambda env: (env[0], -env[1]))
        dp = []
        
        for w, h in envelopes:
            left = bisect_left(dp, h)
            if left == len(dp):
                dp.append(h)
            else:
                dp[left] = h
                
        return len(dp)