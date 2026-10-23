# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            pre = None
            cur = head

            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        dummy = ListNode(-1,head)
        prev = dummy

        while True:
            start = prev.next

            end = prev
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            
            nxt = end.next

            end.next = None
            prev.next = reverse(start)

            start.next = nxt
            prev = start