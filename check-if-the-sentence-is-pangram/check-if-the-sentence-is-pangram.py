import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = dict.fromkeys(string.ascii_lowercase, 0)
        for c in sentence:
            freq[c] += 1
        
        for c in freq:
            if freq[c] == 0:
                return False
            
        return True