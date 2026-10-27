import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        newQueries = sorted([(q,i) for i,q in enumerate(queries)])
        res = []

        hp = []

        j = 0
        for i,(q,idx) in enumerate(newQueries):
            
            while j < len(intervals):
                interval = intervals[j]
                start , end = interval
                if start <= q:
                    heapq.heappush(hp,(end - start + 1,end))
                    j += 1
                else:
                    break
            
            while hp and hp[0][1] < q:
                heapq.heappop(hp)
            if not hp:
                res.append((-1,idx))
            else:
                res.append((hp[0][0],idx))
        
        res.sort(key = lambda x : x[1])
        return [length for length,idx in res]
            