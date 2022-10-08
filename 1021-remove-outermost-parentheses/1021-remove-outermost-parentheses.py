class Solution:
    # two pointers solution
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balanced = 0 # 0 means balanced, otherwise not balanced
        start = 0
        
        for end, char in enumerate(s):
            if char == '(':
                balanced += 1
            elif char == ')':
                balanced -= 1
                
            if balanced == 0:
                # found a valid parentheses
                # remove outermost parentheses and append to result
                valid_parentheses = s[start+1:end]
                res.append(valid_parentheses)
                start = end + 1
                
        return ''.join(res)