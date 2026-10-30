from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            graph[p].append(c)
            in_degree[c] += 1
        
        cnt = 0
        dq = deque() # course don't need prec
        
        for i,indegree in enumerate(in_degree):
            if indegree == 0:
                dq.append(i)
                cnt += 1
            
        while dq:
            for _ in range(len(dq)):
                c = dq.popleft()
                for nxt in graph[c]:
                    if in_degree[nxt] == 0:
                        continue
                    else:
                        in_degree[nxt] -= 1
                        if in_degree[nxt] == 0:
                            dq.append(nxt)
                            cnt += 1
        
        return cnt == numCourses