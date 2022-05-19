# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = float("-inf")
        
        def dfs(root):
            nonlocal longest_path
            
            if not root:
                return 0
            
            left_length = dfs(root.left)
            right_length = dfs(root.right)
            
            path_length = left_length + right_length
            longest_path = max(longest_path, path_length)
            
            return 1 + max(left_length, right_length)
        
        dfs(root)
        
        return longest_path