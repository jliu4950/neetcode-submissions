class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preCourse = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preCourse[crs].append(pre)
        
        def dfs(crs,visitedPath):
            if crs in visitedPath:
                return False
            if preCourse[crs] == []:
                return True
            
            for pre in preCourse[crs]:
                if not dfs(pre,visitedPath|{crs}):
                    return False
            preCourse[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs,set()): return False # if have circle
        return True