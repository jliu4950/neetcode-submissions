# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        st = []
        p = head

        while p:
            st.append(p)
            p = p.next

        res = st[0]
        p = st[0]
        pos = 1

        while pos < len(st):
            p.next = st.pop()
            p = p.next
            if pos < len(st):
                p.next = st[pos]
                p = p.next
                pos += 1

        p.next = None  # ← 关键！切断最后的连接