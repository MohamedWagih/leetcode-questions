class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_start, matched = 0, 0
        freq = {}
        
        for char in s1:
            freq[char] = freq.get(char, 0) + 1  
        
        for win_end in range(len(s2)):
            if s2[win_end] in freq:
                freq[s2[win_end]] -= 1
                if freq[s2[win_end]] == 0:
                    matched += 1
                
            if matched == len(freq):
                return True
            
            if win_end + 1 >= len(s1):
                left_char = s2[win_start]
                win_start += 1
                if left_char in freq:
                    if freq[left_char] == 0:
                        matched -= 1
                    freq[left_char] += 1
                    
        return False