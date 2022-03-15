"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        output = []
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSize = len(queue)
            levelNodes = []
            for _ in range(levelSize):
                node = queue.popleft()
                levelNodes.append(node.val)
                for child in node.children:
                    queue.append(child)
            output.append(levelNodes)
        
        return output