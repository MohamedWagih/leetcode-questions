class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        leaves = []
        
        for word in set(words): # to remove duplicates
            curr = trie
            for char in reversed(word):
                next_char = curr.get(char, {})
                curr[char] = next_char
                curr = next_char
            
            depth = len(word)
            leaves.append([curr, depth+1]) # +1 for the '#'
        
        return sum(depth for node, depth in leaves if len(node)==0)
        