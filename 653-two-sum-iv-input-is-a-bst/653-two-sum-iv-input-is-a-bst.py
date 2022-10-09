# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        candidates = {}
        target = k
        
        def dfs(node):
            
            if not node:
                return False
            
            
            if node.left and dfs(node.left):
                return True
            
            if node.right and dfs(node.right):
                return True
            
            if (target - node.val) in candidates:
                return True
            
            candidates[node.val] = True
            
            return False
            
        return dfs(root)
            
            
             
            
            