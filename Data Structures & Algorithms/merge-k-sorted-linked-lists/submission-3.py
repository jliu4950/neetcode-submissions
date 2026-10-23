# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        idx = 0
        for node in lists:
            if node:
                heapq.heappush(hp,(node.val,idx,node))
            idx += 1
        
        dummy = ListNode(-1)
        p = dummy

        while hp:
            val,index,node = heapq.heappop(hp)
            p.next = node
            p = p.next
            
            nxt = node.next
            if nxt:
                heapq.heappush(hp,(nxt.val,idx,nxt))
                idx += 1
        
        return dummy.next