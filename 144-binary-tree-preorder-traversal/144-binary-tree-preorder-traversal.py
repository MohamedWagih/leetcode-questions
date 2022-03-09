# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderHelper(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.preorderHelper(node.left, result)
        self.preorderHelper(node.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorderHelper(root, result)
        
        return result
