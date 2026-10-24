class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if parent[ra] > parent[rb]:
                ra,rb = rb,ra
            
            parent[ra] = rb
            size[rb] += size[ra]
            return True

        for (x,y) in edges:
            if not union(x,y):
                return False
        
        return True