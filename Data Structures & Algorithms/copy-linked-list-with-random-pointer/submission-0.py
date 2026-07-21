"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=Node(-1)
        p1=dummy

        nodes=[]
        
        p=head
        while p:
            p1.next=Node(p.val)
            p1=p1.next
            
            nodes.append([p,p1])

            p=p.next
        
        for node in nodes:
            # find random
            random=node[0].random
            if random is None:
                node[1].random=None
            else:
                for i in range(len(nodes)):
                    if nodes[i][0]==random:
                        node[1].random=nodes[i][1]
        
        return dummy.next
        