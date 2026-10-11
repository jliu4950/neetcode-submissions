"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        dic = defaultdict(list)
        
        def dfs(node):
            if node in dic:
                return
            
            dic[node] = Node(node.val,[])
            for nx_node in node.neighbors:
                dfs(nx_node)

        dfs(node)
        
        for oldNode,copyNode in dic.items():
            for nei in oldNode.neighbors:
                copyNode.neighbors.append(dic[nei])
        
        return dic[node]