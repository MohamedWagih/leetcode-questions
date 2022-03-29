class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_length = 0
        curr_length = 0
        
        for char in s:
            if char != " ":
                curr_length += 1
            else:
                if curr_length != 0:
                    max_length = curr_length
                curr_length = 0
        
        if curr_length != 0:
            max_length = curr_length

        return max_length