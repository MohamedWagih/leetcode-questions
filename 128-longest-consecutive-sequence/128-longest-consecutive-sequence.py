class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        num_set = set(nums)
        longest_consecutive = 0 
        for num in num_set:
            # to scan number that is not already part of longestConsecutive
            if num-1 not in num_set:
                current_num = num
                current_consecutive = 1
                
                while current_num+1 in num_set:
                    current_num += 1
                    current_consecutive += 1
                
                longest_consecutive = max(longest_consecutive, current_consecutive)
                
        return longest_consecutive
