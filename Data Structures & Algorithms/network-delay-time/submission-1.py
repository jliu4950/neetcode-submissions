from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        visited = set()
        hp = []
        hp.append((0,k))
        res = 0

        while hp:

            time,node = heapq.heappop(hp)
            if node not in visited:
                visited.add(node)
                res = max(res,time)
                for nxt,w in graph[node]:
                    if nxt not in visited:
                        heapq.heappush(hp,(time + w,nxt))
        
        if len(visited) == n:
            return res
        else:
            return -1 