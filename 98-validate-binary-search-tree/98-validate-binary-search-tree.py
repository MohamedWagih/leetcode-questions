# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        def inorderTraversal(root, output):
            if not root:
                return True
            left = inorderTraversal(root.left, output)
            
            if output and root.val <= output[-1]:
                return False
            output.append(root.val)
            
            right = inorderTraversal(root.right, output)
            
            return left and right
        
        return inorderTraversal(root, inorder)