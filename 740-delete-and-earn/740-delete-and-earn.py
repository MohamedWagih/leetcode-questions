class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev_num = None
        max_without_prev, max_with_prev = 0, 0
        
        for num in sorted(count):
            # if current number is adjacent to the previous number 
            if prev_num == num-1:
                # skip taking current number points if we took the previuos number
                # take current number points and take the old points without the previous number
                max_without_prev, max_with_prev = max(max_without_prev, max_with_prev), max_without_prev + num * count[num]
            
            # current number is not adjacent to the previous number
            # so in both cases we can take the maximum previous points
            else:
                # take maximum previous points without currnet 
                # take maximum previous points with currnet
                max_without_prev, max_with_prev = max(max_without_prev, max_with_prev), max(max_without_prev, max_with_prev) + num * count[num]
            
            # update previous number
            prev_num = num
        
        return max(max_without_prev, max_with_prev)