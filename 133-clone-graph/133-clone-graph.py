from collections import deque 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        graph = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        
        while queue:
            curr_node = queue.popleft()
            for n in curr_node.neighbors:
                if n not in graph:
                    queue.append(n)
                    graph[n] = Node(n.val)
                graph[curr_node].neighbors.append(graph[n])
        
        return graph[node]