"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy=defaultdict(Node)
        p=head

        while p:
            oldToCopy[p]=Node(p.val)
            p=p.next
        
        # connect next and random
        
        for orgNode in oldToCopy:
            nxt=orgNode.next
            random=orgNode.random

            copyNode=oldToCopy[orgNode]

            copyNode.next=oldToCopy[nxt] if nxt else None
            copyNode.random=oldToCopy[random] if random else None
        
        return oldToCopy[head] if oldToCopy else None