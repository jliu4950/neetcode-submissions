class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def dfs(node,dst,visited): # if node can reach dst?
            if node not in graph or dst not in graph:
                return False
            if node == dst:
                return True
            if node in visited:
                return False

            visited.add(node)
            for nx in graph[node]:
                if dfs(nx,dst,visited):
                    return True
            
            return False
        
        for (x,y) in edges:
            if dfs(x,y,set()):
                return [x,y]
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            
            graph[x].append(y)
            graph[y].append(x)
        
        return [-1,-1]