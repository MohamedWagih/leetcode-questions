from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_freq = Counter(target)
        arr_freq = Counter(arr)
        
        for num in target_freq:
            if target_freq[num] != arr_freq.get(num,"-1"):
                return False
            
        return True