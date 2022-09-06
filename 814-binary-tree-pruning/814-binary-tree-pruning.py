# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            left_has_ones = False
            right_has_ones = False
            
            if not root.left and not root.right:
                return root.val == 1
            
            if root.left:
                left_has_ones = dfs(root.left)
                if not left_has_ones:
                    root.left = None
                    
            if root.right:
                right_has_ones = dfs(root.right)
                if not right_has_ones:
                    root.right = None
            
            return left_has_ones or right_has_ones or root.val == 1
        
        has_ones = dfs(root)
        if not has_ones:
            root = None
        
        return root
                
            