class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if n == k :
            return total
        
        max_score = 0
        win_start = 0
        win_sum = 0
        for win_end in range(n):
            win_sum += cardPoints[win_end]
            if n - (win_end-win_start+1) == k:
                max_score = max(max_score, total-win_sum)
                win_sum -= cardPoints[win_start]
                win_start += 1

        return max_score