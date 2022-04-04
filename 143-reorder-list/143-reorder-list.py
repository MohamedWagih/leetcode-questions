# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        
        # Get middle of the list
        curr, next = head, head
        while next.next and next.next.next:
            curr = curr.next
            next = next.next.next
        mid = curr.next
        curr.next = None
        
        # push the second half into stack
        stack = []
        while mid:
            stack.append(mid)
            mid = mid.next
        
        # modify the first half to include the second half from stack in between
        curr = head
        while stack and curr:
            next = curr.next
            node = stack.pop()
            curr.next = node
            node.next = next
            curr = next
            