class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

            if size[ra] > size[rb]:
                ra,rb = rb,ra
            
            parent[ra] = rb 
            size[rb] += size[ra]

            return True
        
        cnt = n
        for (x,y) in edges:
            if union(x,y):
                cnt -= 1
        
        return cnt
        