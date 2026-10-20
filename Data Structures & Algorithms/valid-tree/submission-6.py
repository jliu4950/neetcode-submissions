# Union
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        for u,v in edges:
            ru = find(u)
            rv = find(v)

            if ru == rv:
                return False
            
            parent[ru] = rv
        
        return True

        