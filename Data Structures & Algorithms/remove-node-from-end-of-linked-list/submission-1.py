# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[ListNode(-1)]
        p=head

        while p:
            nodes.append(p)
            p=p.next
        nodes[0].next=nodes[1]
        
        pre=nodes[len(nodes)-n-1]
        delNode=nodes[len(nodes)-n]
        pre.next=delNode.next

        return nodes[0].next
        