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
        
        # initialize
        dq = deque([i for i,cnt in enumerate(in_degree) if cnt == 0])
        res = []

        # iterate
        while dq:
            course = dq.popleft()
            res.append(course)
            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    dq.append(c)

        #return 
        return res if len(res) ==  numCourses else []       