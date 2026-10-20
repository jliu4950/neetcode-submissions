class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # detect if have cycle
        if len(edges) != n - 1:
            return False 

        graph = {i:[] for i in range(n)}

        visited = set()

        for e in edges:
            u,v = e
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,parent):
            if node in visited:
                return 
            
            visited.add(node)
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                dfs(nxt,node)
            return
        dfs(0,-1)
        return len(visited) == n