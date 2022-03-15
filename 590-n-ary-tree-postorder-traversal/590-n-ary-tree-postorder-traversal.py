"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return
        
        def postorderHelper(root, output):
            for node in root.children:
                postorderHelper(node, output)
            output.append(root.val)
        
        output=[]
        postorderHelper(root, output)
        return output