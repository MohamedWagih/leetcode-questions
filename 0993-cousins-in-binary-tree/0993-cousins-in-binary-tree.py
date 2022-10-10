# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return None
        
        def findNode(parent, node, level, target):
            if not node:
                return False
            
            if node.val == target:
                return (level, parent)
            
            if node.left or node.right:
                return findNode(node, node.left, level+1, target) or findNode(node, node.right, level+1, target)
            
            return False
        
        x_level, x_parent = findNode(-1,root, 0, x)
        y_level, y_parent = findNode(-1,root, 0, y)
        
        if x_level == y_level:
            if x_parent != y_parent:
                return True
        
        return False
        
        