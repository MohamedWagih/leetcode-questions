class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(" ")
        ordered_words = [""] * len(splitted)
        for word in splitted:
            idx = int(word[-1])-1
            ordered_words[idx] = word[:-1]
        return ' '.join(ordered_words)
        