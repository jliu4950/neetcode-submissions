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
        dic = {}
        def get_copy(node):
            if not node:
                return None
            elif node in dic:
                return dic[node]
            else:
                dic[node] = Node(node.val)
                return dic[node]
        
        cur = head
        while cur:
            copy = get_copy(cur)
            copy.next = get_copy(cur.next)
            copy.random = get_copy(cur.random)
            cur = cur.next
            
        return get_copy(head)
        