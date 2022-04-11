# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        def dfs(node, path_max):
            nonlocal good_nodes
            
            path_max = max(node.val, path_max)
            if node.val == path_max:
                good_nodes += 1
            
            if node.left:
                dfs(node.left, path_max)
            if node.right:
                dfs(node.right, path_max)
        
        dfs(root, float('-inf'))
        
        return good_nodes