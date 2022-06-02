class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]
        
        for num in nums:
            subsets_length = len(all_subsets)
            for i in range(subsets_length):
                all_subsets.append(all_subsets[i] + [num])
        
        return all_subsets