from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        types = Counter(jewels)
        stones_freq = Counter(stones)
        
        total = 0
        for stone in stones_freq:
            if stone in types:
                total += stones_freq[stone]
        return total