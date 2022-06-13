class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 
        
        dp = [[0]*len(triangle) for _ in triangle]
        dp[0][0] = triangle[0][0]
        
        for row in range(1,len(triangle)):
            curr_row = triangle[row]
            for col in range(len(curr_row)):
                
                # if first column, there is one path that we came from
                # which is the first column of the previous row
                if col == 0:
                    dp[row][col] = dp[row-1][col] + triangle[row][col]
                
                # if the last column, there is one path that we came from
                # which is the last column of the previous row
                elif col == len(curr_row)-1:
                    dp[row][col] = dp[row-1][col-1] + triangle[row][col]
                
                # if any column else, we could have came form the same column in the previous row
                # or previous column in the previous row, so we will take the minimum of poth
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1]) + triangle[row][col]

        return min(dp[-1])