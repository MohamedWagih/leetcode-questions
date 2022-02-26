class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0 for _ in range(len(s)+1)]
        dp[0]=1
        if s[0] == '0':
            return 0
        else:
            dp[1]=1
            
        for i in range(2, len(s)+1):
            curr_digit = s[i-1]
            prev_digit = s[i-2]
            if curr_digit == '0':
                if prev_digit == '1' or prev_digit == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0;
            else:
                if prev_digit =='1' or (prev_digit =='2' and curr_digit <= '6'):
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[len(s)]