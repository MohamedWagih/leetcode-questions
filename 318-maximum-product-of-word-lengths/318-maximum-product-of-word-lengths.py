from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = defaultdict(int)
        max_product = 0
        
        for i, word in enumerate(words):
            for char in word:
                mask[word] |= 1 << (ord(char) - ord('a'))
            
            for j in range(i):
                if mask[word] & mask[words[j]] == 0:
                     max_product = max(max_product, len(word) * len(words[j]))
        
        return max_product