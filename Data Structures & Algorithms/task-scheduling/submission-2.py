import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        hp = []
        for task in tasks:
            dic[task] = dic.get(task,0)+1
        
        for task,freq in dic.items():
            heapq.heappush(hp,(-freq ,task))
        
        #模拟任务过程：
        time = 0
        cool = deque()
        while hp or cool :
            time +=1
            
            if hp: 
                freq , task =heapq.heappop(hp)
                if - freq >1:
                    cool.append((task , time + n , freq +1))

            if cool and cool[0][1]==time:
                task , waittime ,freq = cool.popleft()
                heapq.heappush(hp,(freq ,task))
        
        return time