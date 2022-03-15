# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return 
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        left, right = False, False
        if root.left:
            left = self.hasPathSum(root.left, targetSum-root.val)
        if root.right:
            right = self.hasPathSum(root.right, targetSum-root.val)
        
        return left or right