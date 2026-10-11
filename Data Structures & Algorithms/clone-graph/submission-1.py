"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        dic = defaultdict(list)

        def dfs(node):
            if node in dic:
                return dic[node]
            
            copyNode = Node(node.val,[])
            dic[node] = copyNode

            for nei in node.neighbors:
                copynei = dfs(nei)
                copyNode.neighbors.append(copynei)
            
            return copyNode
        
        return dfs(node)