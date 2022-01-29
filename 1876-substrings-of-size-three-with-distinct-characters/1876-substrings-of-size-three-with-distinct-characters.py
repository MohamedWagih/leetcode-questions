class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        chars = {}
        win_start = 0
        count = 0
        for win_end in range(len(s)):
            if s[win_end] in chars and chars[s[win_end]] >= win_start:
                win_start = chars[s[win_end]] + 1
            
            chars[s[win_end]] = win_end
            
            if win_end - win_start + 1 == 3:
                count += 1
                win_start += 1 
        return count
                