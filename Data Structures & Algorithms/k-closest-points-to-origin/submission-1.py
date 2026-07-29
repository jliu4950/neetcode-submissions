import heapq

class Solution:
    def kClosest(self, points,k):
        hp = []

        for point in points:
            heapq.heappush(hp,(-(point[0]**2 + point[1]** 2),point[0] , point[1]))
            if len(hp) > k:
                heapq.heappop(hp)
        
        res = []
        for _ in range(k):
            d,x,y = heapq.heappop(hp)
            res.append([x,y])
        
        return res