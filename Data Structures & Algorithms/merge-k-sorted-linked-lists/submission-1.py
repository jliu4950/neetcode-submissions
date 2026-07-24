# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists)>1:
            merge=[]
            s=0
            f=1
            while f<len(lists):
                mergedList=self.mergeTwoList(lists[s],lists[f])
                merge.append(mergedList)
                s+=2
                f+=2

            if s==len(lists)-1:
                merge.append(lists[-1])
            
            lists=merge
        
        return lists[0] if lists else None
    
    def mergeTwoList(self,p1,p2):
        dummy=ListNode(-1)
        p=dummy
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
        