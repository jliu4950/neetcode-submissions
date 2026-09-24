class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        def dfs(i):
            if i <= 1:
                return 1
            if cache[i] != 0:
                return cache[i]
            else:
                cache[i] = dfs(i - 1) + dfs(i - 2)
            #print(i,res)
            return  cache[i]
        
        return dfs(n)
        