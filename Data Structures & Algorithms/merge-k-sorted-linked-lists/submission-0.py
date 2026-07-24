# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        if lists:
            dummy.next=lists[0]

        for i in range(1,len(lists)):
            p=dummy
            p1=dummy.next
            p2=lists[i]

            while p1 and p2:
                if p1.val<=p2.val:
                    p.next=p1
                    p1=p1.next
                else:
                    p.next=p2
                    p2=p2.next
                
                p=p.next
            
            p.next=p1 if p1 else p2
        
        return dummy.next
        