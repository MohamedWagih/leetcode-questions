class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs))]
        
        def knapsack(idx, zeros_count, ones_count):
            if idx==len(strs) or (ones_count==0 and zeros_count==0):
                return 0
            
            if dp[idx][zeros_count][ones_count] == -1:
                curr_zeros=strs[idx].count("0")
                curr_ones=strs[idx].count("1")
                
                if curr_zeros > zeros_count or curr_ones > ones_count:
                    dp[idx][zeros_count][ones_count] = knapsack(idx+1, zeros_count, ones_count)
                
                else:
                    include = 1 + knapsack(idx+1, zeros_count - curr_zeros, ones_count - curr_ones)
                    exclude = knapsack(idx+1, zeros_count, ones_count)
                    dp[idx][zeros_count][ones_count] = max(include, exclude)
            
            return dp[idx][zeros_count][ones_count]
        
        
        return knapsack(0, m, n)