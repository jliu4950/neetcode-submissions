# BFS版本
'''
1.
in_degree:记录每个点的入度
graph
dq

'''
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            graph[p].append(c)
            in_degree[c] += 1
        
        cnt = 0
        dq = deque([i for i in range(numCourses) if in_degree[i] == 0]) # course don't need prec

        # 注意这一段的优化，我自己写的时候非常复杂 
        while dq:
            course = dq.popleft() # 入度为0的课程在弹出来的时候进行记录数量
            cnt += 1
            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    dq.append(c) # 入度为0的课程才能加入队列
        
        return cnt == numCourses