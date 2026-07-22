# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        p=dummy
        quotient=0
        remainder=0

        while l1 and l2:
            remainder=(l1.val+l2.val+quotient)%10
            quotient=(l1.val+l2.val+quotient)//10
            print(f"quotient:{quotient},remainder:{remainder}")
            p.next=ListNode(remainder)
            p=p.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            remainder=(l1.val+quotient)%10
            quotient=(l1.val+quotient)//10
            p.next=ListNode(remainder)
            p=p.next
            l1=l1.next
        
        while l2:
            remainder=(l2.val+quotient)%10
            quotient=(l2.val+quotient)//10
            p.next=ListNode(remainder)
            p=p.next
            l2=l2.next
        
        if quotient !=0:
            p.next=ListNode(quotient)
        
        return dummy.next




        