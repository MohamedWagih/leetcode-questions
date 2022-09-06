# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return False
            
            left_has_ones = dfs(root.left)
            right_has_ones = dfs(root.right)
            
            if not left_has_ones:
                root.left = None

            if not right_has_ones:
                root.right = None
            
            return left_has_ones or right_has_ones or root.val == 1
        
        return root if dfs(root) else None
                
            