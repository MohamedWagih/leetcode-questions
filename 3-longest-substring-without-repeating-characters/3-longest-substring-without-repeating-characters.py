class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_start = 0
        longest = 0
        pos = {}
        for win_end in range(len(s)):
            curr_char = s[win_end]

            if curr_char in pos:
                win_start = max(win_start, pos[curr_char]+1)
            pos[curr_char] = win_end
            
            longest = max(longest, win_end-win_start+1)
        
        return longest
            