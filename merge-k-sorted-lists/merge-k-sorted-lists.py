# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap=[]
        res_head = ListNode(0)
        curr = res_head
        finished = False
        while not finished:
            finished = True
            for i in range(len(lists)):
                if lists[i]:
                    finished = False
                    print(lists[i].val)
                    heapq.heappush(min_heap, lists[i].val)
                    lists[i] = lists[i].next
            if min_heap:
                min_val = heapq.heappop(min_heap)
                curr.next = ListNode(min_val)
                curr = curr.next
            
        while min_heap:
            min_val = heapq.heappop(min_heap)
            curr.next = ListNode(min_val)
            curr = curr.next
            
        return res_head.next
        