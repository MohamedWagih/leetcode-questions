class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for idx, char in enumerate(s):
            if freq[char] == 1:
                return idx
        
        return -1