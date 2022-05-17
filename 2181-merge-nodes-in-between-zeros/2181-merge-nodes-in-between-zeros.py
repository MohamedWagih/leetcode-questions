# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        merged_list_head = ListNode(0)
        curr_modified = merged_list_head
        curr = head.next
        curr_sum = 0
        
        while curr:
            if curr.val == 0:
                curr_modified.next = ListNode(curr_sum)
                curr_modified = curr_modified.next
                curr_sum = 0
            else:
                curr_sum += curr.val
            curr = curr.next
        
        return merged_list_head.next