# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        
        def postorderTraversalHelper(root, output):
            if root.left:
                postorderTraversalHelper(root.left, output)
            if root.right:
                postorderTraversalHelper(root.right, output)
            output.append(root.val)
        
        output = []
        postorderTraversalHelper(root, output)
        return output
        