class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue=[]
        queue.append(beginWord)
        level = 1
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.pop(0)
                if curr_word == endWord:
                    return level
                for i in range(len(curr_word)):
                    for c in range(ord('a'), ord('z')+1):
                        new_word = curr_word[:i] + chr(c) + curr_word[i+1:]
                        if new_word in wordSet and new_word != curr_word:
                            queue.append(new_word)
                            wordSet.remove(new_word)
            level += 1

        return 0