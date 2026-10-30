# DFS版本
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        visit = [0] * numCourses # 0: not visit 1:visiting 2:finished

        for c,p in prerequisites:
            graph[p].append(c)
        
        # dfs: from start to c, 
        # if there is a cycle :return False
        # else :return True
        def dfs(c):
            if visit[c] == 1:
                return False
            if visit[c] == 2:
                return True
            
            visit[c] = 1
            for course in graph[c]:
                if not dfs(course):
                    return False
            visit[c] = 2 # c及后面的点都没有环
            return True
        
        for c in range(numCourses):
            if visit[c] == 0:
                if not dfs(c):
                    return False
        
        return True