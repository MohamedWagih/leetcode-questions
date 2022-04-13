class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        
        left, right = 0, 1
        max_profit = float('-inf')
        
        while right < n:
            curr_profit = prices[right] - prices[left]
            max_profit = max(max_profit, curr_profit)
            
            # if right price < left price so there is a lower price to buy at 
            if prices[right] < prices[left]:
                left = right
            
            right += 1
            
        if max_profit < 0:
            return 0
        
        return max_profit