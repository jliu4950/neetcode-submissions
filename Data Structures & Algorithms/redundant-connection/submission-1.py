# DFS
# 无向图判断是否有环：用parent
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        visited = set()

        def dfs(node,parent):
            if node in visited:
                return True
            
            visited.add(node)
            for nx in graph[node]:
                if nx != parent:
                    if dfs(nx,node):
                        return True
            
            return False
        
        for (x,y) in edges:
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []

            graph[x].append(y)
            graph[y].append(x)

            visited = set()
            if dfs(x,-1):
                # print([x,y])
                return [x,y]