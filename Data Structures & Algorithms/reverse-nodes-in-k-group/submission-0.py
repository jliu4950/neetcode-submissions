# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1) # 需要dummy ，不然无法找到链表的头
        pre=dummy
        p=head
        while p:
            start,end,nxt=self.reverse(p,k)
            pre.next=start
            pre=end
            p=nxt
        
        return dummy.next

    def reverse(self,head,k):
        # nodes less than k,返回原链表
        p=head
        i=0
        while i<k and p:
            p=p.next
            i+=1
        if i<k:
            return head,p,None
        
        # if len(nodes)>k,返回反转链表头和尾
        pre=None
        cur=head
        nxt=head.next
        while k>0 and cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
            k-=1
        
        return pre,head,nxt #注意返回值
        
        # None<- 1 <- 2 <- 3 -> 4
        #                  cur  nxt   
