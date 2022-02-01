class Solution:
    def pair_with_target_Sum(self, target_sum, nums, left, triplets):
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            
            if curr_sum == target_sum :
                triplets.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif curr_sum < target_sum:
                left += 1
            else:
                right -= 1 
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.pair_with_target_Sum(-nums[i], nums, i+1, triplets )
        return triplets 
    
    