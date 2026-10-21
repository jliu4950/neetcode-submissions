class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges) + 1))

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x,y):
            nx = find(x)
            ny = find(y)

            if nx == ny:
                return False
            else:
                parent[nx] = ny
                return True
        
        for (x,y) in edges:
            if not union(x,y):
                return [x,y]
        
        