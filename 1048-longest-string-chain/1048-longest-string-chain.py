'''
DP Bottom-Up approach:

    - First we will sort the words with there length to ensure the previous word length is
      less than current word.
    
    - Loop throught every word and with every word try to remove one character at a time:
        current word longest chain would be max of all its predecessors.
    
    - Return Longest possible word chain of all words 
'''
from collections import defaultdict
class Solution:
    # time : O(n*l) where n is words length and L is word length
    # space: O(n)
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        longest_chain = 0
        dp = defaultdict(int)
        
        for word in words:
            dp[word] = 1 # trivial word chain
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                # if predecessor is presented in words and has a longest chain
                if dp[predecessor] + 1 > dp[word]:
                    dp[word] = dp[predecessor] + 1
            
            # longest chain of all words        
            longest_chain = max(longest_chain, dp[word])
        
        return longest_chain