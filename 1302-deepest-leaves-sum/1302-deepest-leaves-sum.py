# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_leaves = []
        max_depth = 0
        def get_max_depth(root, level):
            nonlocal max_depth
            if not root:
                return
            if root.left:
                get_max_depth(root.left, level + 1)
            if root.right:
                get_max_depth(root.right, level + 1)
            max_depth = max(level, max_depth)
        
        get_max_depth(root, 0)
        
        def dfs(root, level):
            if not root:
                return
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
            if level == max_depth:
                deepest_leaves.append(root.val)
                
        dfs(root, 0)
        
        return sum(deepest_leaves)
        
        
        