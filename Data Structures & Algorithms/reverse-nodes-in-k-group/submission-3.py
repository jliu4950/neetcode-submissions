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

            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
        
        dummy = ListNode(-1,head)
        prev = dummy

        while True:
            start = prev.next

            end = prev
            for _ in range(k):
                if not end.next:
                    return dummy.next
                end = end.next
            
            nxt = end.next

            reverse(start)

            prev.next = end
            start.next = nxt
            prev = start