from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {'{':'}', '(':')', '[':']'}
        stack = []
        
        for c in s:
            if c =='(' or c=='{' or c=='[':
                stack.append(c)
            else:
                if len(stack) == 0 or parentheses_map[stack[-1]] != c:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True
                    