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
        '''
        dic = {old node: new node}
        when meet a node not in dic,create it
        '''
        
        dic = {}

        def copy_node(node):
            if node is None:
                return None
            if node not in dic:
                dic[node] = Node(node.val)
            return dic[node]

        cur = head
        while cur:
            copy = copy_node(cur)
            copy.next = copy_node(cur.next)
            copy.random = copy_node(cur.random)
            cur = cur.next
        return copy_node(head)
            