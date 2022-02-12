from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Wrapper():
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
    
class Solution:
    
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tail = None
        
        queue = PriorityQueue()
        
        for l in lists:
            if l:
                queue.put(Wrapper(l))
        
        while not queue.empty():
            node = queue.get().node
            
            if head == None:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            
            if node.next is not None:
                queue.put(Wrapper(node.next))
        
        return head
            