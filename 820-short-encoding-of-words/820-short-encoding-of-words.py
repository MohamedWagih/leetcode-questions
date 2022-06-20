class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        '''
        - Will try to remove every suffix for every word in words:
            words = ["time", "me", "bell"] ===> s = "time#bell#"
            as you see 'me' is a suffix of 'time' so no need to represent 'me'
        - Words[i].length <= 7s= so words[i] only has 7 suffixes 
        - The asnwer would be sum(word.length + 1 for word in words) after removing suffixes
        '''
        words_set = set(words)
        
        for word in words:
            for i in range(1, len(word)):
                words_set.discard(word[i:])
        
        return sum((len(word) + 1) for word in words_set)
        