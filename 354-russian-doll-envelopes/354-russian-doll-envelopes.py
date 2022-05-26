class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        
        # we sorted it with (width) so we are left with the (height) to find the longest increasing (height)
        # but we sort in deacreasing (height) in case of equal (width) 
        envelopes.sort(key= lambda env: (env[0], -env[1]))
        dp = []
        
        for w, h in envelopes:
            # find the position to insert the new H 
            i = bisect_left(dp, h)
            
            if i == len(dp):
                dp.append(h)    
            else:
                dp[i] = h
                
        return len(dp)