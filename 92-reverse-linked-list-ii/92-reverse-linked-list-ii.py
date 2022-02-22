# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        prev, curr = None, head
        count = 0
        while curr and count < left-1:
            prev = curr
            curr = curr.next
            count += 1
        
        last_node_left_part = prev
        last_node_after_reverse = curr
        
        next = None
        while curr and count < right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
            
        if last_node_left_part: 
            last_node_left_part.next = prev
        # if P == 1 so we reversed starting from the head we need to update it
        else:
            head = prev
            
        last_node_after_reverse.next = curr
        
        return head
        