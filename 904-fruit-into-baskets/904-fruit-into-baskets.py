class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        maxNum = float("-inf")
        winStart = 0
        for winEnd in range(len(fruits)):
            freq[fruits[winEnd]] = freq.get(fruits[winEnd], 0) + 1 
            while len(freq) > 2:
                freq[fruits[winStart]] -= 1
                if freq[fruits[winStart]] == 0:
                    del freq[fruits[winStart]]
                winStart += 1
            maxNum = max(maxNum, winEnd - winStart +1)
        
        return maxNum