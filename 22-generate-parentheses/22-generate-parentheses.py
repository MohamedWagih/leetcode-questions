from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque()
        
        # queue entry [ parentheses_string, open_count, closed_count]
        queue.append(["", 0, 0])
        
        while queue:
            curr_parentheses, open_count, closed_count = queue.popleft()

            if open_count < n:
                queue.append([curr_parentheses+"(", open_count+1, closed_count])

            if open_count - closed_count > 0:
                queue.append([curr_parentheses+")", open_count, closed_count+1])

            if len(curr_parentheses) == n*2:
                result.append(curr_parentheses)
        
        return result