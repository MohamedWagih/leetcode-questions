from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result=[]
        queue=deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            val = None
            for _ in range(n):
                node = queue.popleft()
                val = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # store the last value in the level
            result.append(val)
        
        return result
        
      # DFS
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def dfs(node, curr_lvl, max_lvl):
#             if not node: return
#             if curr_lvl >= max_lvl[0]:
#                 res.append(node.val)
#                 max_lvl[0] += 1
#             if node.right:
#                 dfs(node.right, curr_lvl+1, max_lvl)
#             if node.left:
#                 dfs(node.left, curr_lvl+1, max_lvl)
        
#         max_lvl = [0]
#         dfs(root,0, max_lvl)
#         return res