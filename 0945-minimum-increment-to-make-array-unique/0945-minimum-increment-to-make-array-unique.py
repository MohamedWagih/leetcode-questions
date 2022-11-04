class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq = {}
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
        moves = 0
        duplicates = []
        
        max_val = max(nums)
        max_val_needed = len(nums) + max_val
        
        for num in range(max_val_needed):
            if freq.get(num, 0) >= 2:
                duplicates += [num] * (freq[num]-1)
            
            elif duplicates and freq.get(num, 0) == 0:
                moves +=  num - duplicates.pop()
        
        return moves
                
            
        
        