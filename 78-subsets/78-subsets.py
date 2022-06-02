class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_subsets = []
        
        def backtrack(idx, curr_subset):
            all_subsets.append(curr_subset[:])
            
            for i in range(idx, n):
                curr_subset.append(nums[i])
                backtrack(i+1, curr_subset)
                curr_subset.pop()
        
        
        backtrack(0,[])
        
        return all_subsets