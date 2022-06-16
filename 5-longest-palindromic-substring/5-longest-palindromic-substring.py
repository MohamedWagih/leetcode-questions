class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_start = 0        
        longest_len = 1
        
        for i in range(0,n):
            right = i
            while right < n and s[right] == s[i]:
                right += 1
            
            left = i-1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            # now s[ left : right ] execlusive is palindrome 
            curr_len = right - left - 1
            if curr_len > longest_len:
                longest_len = curr_len
                longest_start = left+1
                            
        
        return s[longest_start: longest_start+longest_len]
                    