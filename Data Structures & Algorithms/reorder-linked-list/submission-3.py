# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        
        mid=s # 注意，前面还连着mid呢
        #reverse
        pre=None
        cur=mid
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        
        dummy=ListNode(-1)
        p=dummy
        p1=head
        p2=pre
        
        while p1 and p2:
            if p1==p2:
                break
            p.next=p1
            p=p.next
            p1=p1.next

            p.next=p2
            p=p.next
            p2=p2.next
        
        p.next=p2