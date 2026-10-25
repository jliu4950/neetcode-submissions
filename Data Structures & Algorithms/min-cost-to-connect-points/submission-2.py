from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                xi,yi = points[i]
                xj,yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                graph[i].append((cost,j))
                graph[j].append((cost,i))
        
        visited = set()
        hp = [(0,0)]
        res = 0

        while hp:
            c,i = heapq.heappop(hp)
            if i in visited:
                continue
            visited.add(i)
            res += c

            for cost,j in graph[i]:
                if j not in visited:
                    heapq.heappush(hp,(cost,j))
        
        return res