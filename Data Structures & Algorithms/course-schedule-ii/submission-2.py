# BFS版本
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        graph = {i:[] for i in range(numCourses)}
        
        # build graph
        for c,p in prerequisites:
            graph[p].append(c)
            in_degree[c] += 1

        # 初始化
        dq = deque() # 放的是入度已经为0的课程
        res = []
        for c,indegree in enumerate(in_degree):
            if indegree == 0:
                dq.append(c)
                res.append(c)
        
        # 遍历
        while dq:
            for _ in range(len(dq)):
                p = dq.popleft()
                for c in graph[p]:
                    in_degree[c] -= 1
                    if in_degree[c] == 0:
                        dq.append(c)
                        res.append(c)

        #return 
        return res if len(res) ==  numCourses else []       