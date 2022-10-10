# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getMaxDepth(node, curr_max):
            
            if not node:
                return curr_max
            
            left_depth, right_depth = curr_max, curr_max
            
            if node.left:
                left_depth = getMaxDepth(node.left, curr_max+1)
                
            if node.right:
                right_depth = getMaxDepth(node.right, curr_max+1)
            
            return max(left_depth, right_depth)
        
        return getMaxDepth(root, 1)