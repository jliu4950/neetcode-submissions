# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        groupPrev=dummy
        groupCur=head
        
        while groupCur:
            kthNode=self.getkth(groupPrev,k)
            if not kthNode:
                break
            groupNext=kthNode.next
            
            i=0
            pre=groupPrev
            cur=groupCur
            while i<k:
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
                i+=1
            
            groupPrev.next=kthNode
            groupCur.next=groupNext

            #update
            groupPrev=groupCur
            groupCur=groupNext
        
        return dummy.next

    def getkth(self,node,k):
        
        while k>0:
            if not node:
                return None
            node=node.next
            k-=1
        
        return node
