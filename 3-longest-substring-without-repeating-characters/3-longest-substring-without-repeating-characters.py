from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_start = 0
        longest = 0
        positions = defaultdict(int)
        
        for win_end in range(len(s)):
            if s[win_end] in positions and positions[s[win_end]] >= win_start:
                win_start = positions[s[win_end]] + 1 
            
            positions[s[win_end]] = win_end
            
            longest = max(longest, win_end - win_start + 1)
        
        return longest