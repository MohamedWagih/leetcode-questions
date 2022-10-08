class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        
        for c in s:
            if stack1 and c == '#':
                stack1.pop()
            
            elif c != "#":
                stack1.append(c)
        
        for c in t:
            if stack2 and c == '#':
                stack2.pop()
            
            elif c != "#":
                stack2.append(c)
        
        while stack1 and stack2:
            if stack1.pop() != stack2.pop():
                return False
        
        if stack1 or stack2:
            return False
        
        return True

        