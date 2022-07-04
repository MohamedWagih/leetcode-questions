class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ltr = [1 for _ in range(n)]
        rtl = [1 for _ in range(n)]
        
        # left to right traversal
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ltr[i] = ltr[i-1] + 1
        
        # right to left traversal
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rtl[i] = rtl[i+1] + 1
        
        total_candies = 0
        for i in range(n):
            total_candies += max(ltr[i], rtl[i])
        
        return total_candies