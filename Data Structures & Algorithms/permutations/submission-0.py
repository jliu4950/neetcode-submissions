class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i,s):
            if i == n :
                ans.append(path[:])
                return

            for x in s:
                path.append(x)
                dfs(i + 1, s - {x})
                path.pop()

        dfs(0,set(nums))
        return ans
