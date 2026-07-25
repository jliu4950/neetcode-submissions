# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        p=dummy
        hp=[]
        
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(hp,(node.val,i,node)) # 当node的值相当时，i可以作为第二比较对象
        cnt=0
        while hp:
            val,i,node=heapq.heappop(hp)
            p.next=node
            p=p.next #忘记挪动了

            if node.next: #没有做判断
                heapq.heappush(hp,(node.next.val,cnt,node.next))
                cnt+=1

        return dummy.next
        