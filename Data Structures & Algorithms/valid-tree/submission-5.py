# BFS
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # detect if have cycle
        if len(edges) != n - 1:
            return False 

        graph = {i:[] for i in range(n)}

        for e in edges:
            u,v = e
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        q = deque()

        q.append(0)
        visited.add(0)

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                for node in graph[cur]:
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
        
        return len(visited) == n
