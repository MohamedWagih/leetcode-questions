class Solution:
    # O(nlogn + n^2) => O(n^2)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(nlogn)
        nums.sort()
        min_diff = float('+inf')
        closestSum = 0
        
        # x + y + z = target
        # y + z = target - x
        # we need to find (y+z) closest to (target-x)
        
        # O(n)
        for i in range(len(nums)):
                
            left, right = i+1, len(nums)-1
            curr_target = target-nums[i]
            
            # O(n)
            while left<right:
                curr_diff = target - nums[i] - nums[left] - nums[right]
                
                if abs(curr_diff) < abs(min_diff):
                    min_diff = curr_diff
                    closestSum = nums[i] + nums[left] + nums[right]
                    
                if curr_diff == 0:
                    return target
                
                if curr_diff > 0:
                    left += 1
                else:
                    right -= 1
        
        return closestSum