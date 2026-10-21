class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for (u,v) in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        # dfs mark every connected components
        def dfs(node): 
            if node in visited:
                return
            
            visited.add(node)
            for nx in graph[node]:
                dfs(nx)
            return    

        #
        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        return res
            