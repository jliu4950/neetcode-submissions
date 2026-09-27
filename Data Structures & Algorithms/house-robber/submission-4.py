class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [ -1 ] * n
        def dfs(i):
            print(i)
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            else:
                cache[i] = max(dfs(i - 1),dfs(i - 2) + nums[i])
                return cache[i]
        return dfs(n - 1)
