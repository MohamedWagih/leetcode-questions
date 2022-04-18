# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, left_bound, right_bound):
            if not root:
                return True
            if not (root.val > left_bound and root.val < right_bound):
                return False
            
            left = isValid(root.left, left_bound, root.val)
            right = isValid(root.right, root.val, right_bound)
            
            return left and right
        
        return isValid(root, float('-inf'), float('inf'))