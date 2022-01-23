from collections import deque

class Solution:
    def rotate_helper(self, s, b) -> str:
        n = len(s)
        return s[n-b:] + s[:n-b]

    def add_helper(self, s, a) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = str((int(s[i])+a)%10)
        return ''.join(s)
    
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        smallest = s
        visited = set()
        queue = deque([s])
        
        while queue:
            possible = queue.popleft()

            if possible < smallest:
                smallest = possible
            
            add = self.add_helper(possible, a)
            reotated = self.rotate_helper(possible, b)
            
            if add not in visited:
                queue.append(add)
                visited.add(add)
            if reotated not in visited: 
                queue.append(reotated)
                visited.add(reotated)
        
        return smallest