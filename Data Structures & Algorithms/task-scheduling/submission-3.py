import heapq
from collections import deque,Counter
class Solution:
    # def leastInterval(self, tasks , n) -> int:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        time = 0
        cool = deque()

        while cool or maxheap:
            time +=1 #❗️ time怎么利用呢
            
            if maxheap :
                cnt = 1 + heapq.heappop(maxheap)
                if cnt < 0:
                    cool .append([cnt ,time + n]) #只要每次记录好下次用这个task是什么时候就行了，time + n
            
            if cool and cool[0][1] == time :
                cnt = cool.popleft()[0]
                heapq.heappush(maxheap,cnt)
        
        return time