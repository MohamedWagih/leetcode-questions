class Solution:
    # O(nlogn + n) => O(nlogn)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # O(nlogn)
        points.sort(key=lambda p:p[0])
        
        start, end = 0, 1
        total_arrows = 0
        curr_interval = [points[0][start], points[0][end]]
        
        # O(n)
        for i in range(len(points)):

            if points[i][start] <= curr_interval[end]:
                curr_interval[end] = min(curr_interval[end], points[i][end])
                
            elif points[i][start] > curr_interval[end]:
                total_arrows += 1
                curr_interval = points[i]
        
        total_arrows += 1
        
        return total_arrows