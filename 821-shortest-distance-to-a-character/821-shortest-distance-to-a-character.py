class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        
        smallest_distance = float("-inf")
        for i, char in enumerate(s):
            if char == c:
                smallest_distance = i
            result.append(i - smallest_distance)
        
        smallest_distance = float("inf")
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                smallest_distance = i
            result[i] = min(result[i], smallest_distance - i)
        
        return result