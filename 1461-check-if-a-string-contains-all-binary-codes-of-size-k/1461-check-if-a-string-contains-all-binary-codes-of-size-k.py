class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # total number of binary code of length k are exactly 2^k (1<<k)
        total_nums_count =  1 << k
        found = set()
        
        # check every substring of length k
        i = 0
        while i+k <= len(s):
            curr_substring = s[i:i+k]
            if curr_substring not in found:
                found.add(curr_substring)
            if len(found) == total_nums_count:
                return True
            i += 1

        return False