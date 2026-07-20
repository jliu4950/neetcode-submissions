# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not list1 or not list2:
            return list1 if list1 else list2
        
        newhead=None
        if list1.val<=list2.val: # 小的放前面
            #print(f"list1[{list1.val}]")
            list1.next=self.mergeTwoLists(list1.next,list2)
            newhead=list1
        else :
            #print(f"list2[{list2.val}]")
            list2.next=self.mergeTwoLists(list1,list2.next)
            newhead=list2
        return newhead