class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 26
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    # time: O(m) m is word length    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] == None:
                node = TrieNode(char)
                curr.children[i] = node
            
            curr = curr.children[i]
        
        curr.is_word = True
    
    def searchHelper(self, prefix):
            curr = self.root
            for char in prefix:
                i = ord(char) - ord('a')
                if curr.children[i]:
                    curr = curr.children[i]
                else:
                    return None
            return curr
    
    # time: O(m) m is word length
    def search(self, word: str) -> bool:
        node = self.searchHelper(word)
        return node != None and node.is_word
    
    # time: O(m) m is prefix length
    def startsWith(self, prefix: str) -> bool:
        node = self.searchHelper(prefix)
        return node != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)