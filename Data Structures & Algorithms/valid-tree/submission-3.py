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
        
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            
            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt)
            return
        dfs(0)
        return len(visited) == n