# Kruskal算法:把所有边从小到大排序，依次加入，会形成环就跳过
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

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
        
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                xi,yi = points[i]
                xj,yj = points[j]
                
                cost = abs(xi - xj) + abs(yi - yj)
                edges.append((cost,(i,j)))
        edges.sort(key = lambda x:x[0])

        cnt = n
        res = 0
        for c,(i,j) in edges:
            if cnt == 1:
                break
            if union(i,j):
                res += c
                cnt -= 1
        
        return res
