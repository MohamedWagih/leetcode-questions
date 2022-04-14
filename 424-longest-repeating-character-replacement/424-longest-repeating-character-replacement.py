from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win_start = 0
        longest = 0
        freq = defaultdict(int)
        
        for win_end in range(len(s)):
            char = s[win_end]
            freq[char] += 1
            win_length = win_end - win_start + 1
            
            while win_length - max(freq.values()) > k:
                freq[s[win_start]] -= 1
                win_start += 1
                win_length = win_end - win_start + 1
            
            longest = max(longest, win_length)
        
        return longest
        