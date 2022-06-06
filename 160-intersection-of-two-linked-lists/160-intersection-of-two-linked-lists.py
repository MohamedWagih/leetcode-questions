# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA, currB = headA, headB
        sizeA, sizeB = 0, 0
        
        while currA:
            sizeA += 1
            currA = currA.next
        while currB:
            sizeB += 1
            currB = currB.next
        
        if sizeA > sizeB:
            skip = sizeA - sizeB
            while headA and skip:
                headA = headA.next
                skip -= 1
        else:
            skip = sizeB - sizeA
            while headB and skip:
                headB = headB.next
                skip -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return
