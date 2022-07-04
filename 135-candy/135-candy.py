class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]
        
        # left to right traversal
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # last element already have no elements on its right 
        # so we include it in the sum
        total_candies = candies[-1]
        
        # right to left traversal
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
            
            total_candies += candies[i]
        
        return total_candies