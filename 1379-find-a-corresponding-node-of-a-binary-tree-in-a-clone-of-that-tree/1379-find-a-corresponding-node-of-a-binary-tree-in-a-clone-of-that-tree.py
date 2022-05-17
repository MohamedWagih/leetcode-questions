from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        queue = deque()
        queue.append(cloned)
        
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr.val == target.val:
                    return curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)