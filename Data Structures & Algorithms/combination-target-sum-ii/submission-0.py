class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)

        def dfs(i,remain):
            if remain == 0:
                ans.append(path[:])
                return
            if i == n or candidates[i] > remain:
                return
            
            for j in range(i , n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                dfs(j + 1, remain - candidates[j])
                path.pop()    
        
        candidates.sort()
        dfs(0 ,target)
        return ans

        