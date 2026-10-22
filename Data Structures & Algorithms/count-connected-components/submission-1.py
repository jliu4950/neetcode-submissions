class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(a,b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False
            else:
                parent[ra] = rb
                return True
        
        count = n

        for (u,v) in edges:
            if union(u,v):
                count -= 1
        
        return count