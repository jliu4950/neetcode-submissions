import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        cnt = 0

        for point in points:
            x = point[0]
            y = point[1] # ? 如果是相同值，是否也算作答案
            dis = x**2 + y**2
            cnt +=1
            heapq.heappush(hp,(dis,cnt,x,y))
        
        res = []
        for _ in range(k):
            cur = heapq.heappop(hp)
            res.append([cur[2],cur[3]])
        
        return res