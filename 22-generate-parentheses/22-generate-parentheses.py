from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        queue = deque()
        queue.append(["", 0, 0])
        
        while queue:
            level = len(queue)
            for _ in range(level):
                curr_parenthesis, open_count, closed_count = queue.popleft()

                if open_count < n:
                    queue.append([curr_parenthesis+"(", open_count + 1, closed_count])

                if  open_count - closed_count > 0:
                    queue.append([curr_parenthesis+")", open_count, closed_count + 1])

                if len(curr_parenthesis) == n*2:
                    result.append(curr_parenthesis)
        
        return result