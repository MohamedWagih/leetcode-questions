# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,left, right):
        if not left:
            return right
        if not right:
            return left
        
        result = ListNode(-1) 
        curr = result
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return result.next
            
        

    def merge_sort(self, head):
        if head == None or head.next == None:
            return head
            
        mid = self.mid(head)
        right_head = mid.next
        mid.next = None
        
        left = self.merge_sort(head)
        right = self.merge_sort(right_head)
        
        sorted = self.merge(left, right)
        return sorted
        

    def mid(self, head):
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)
        
        
        
        
        
        