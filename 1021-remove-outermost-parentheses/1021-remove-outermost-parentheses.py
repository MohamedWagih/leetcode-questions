class Solution:
    '''
    stack soltion
    
    we use the stack to calculate valid paranthesses and with each valid one append it to output
    ''' 
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        stack = []
        basket = ''
        
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            
            basket += c
            
            # if stack is empty so we have valid paranthesses in basket
            if not stack:
                res += basket[1:-1]
                basket = ''
            
        return res