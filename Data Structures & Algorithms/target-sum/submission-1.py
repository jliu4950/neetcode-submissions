class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = target + sum(nums)
        
        if target < 0 or target % 2:
            return 0 
        
        target = target // 2

        n = len(nums)

        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1 # 初始化

        for i in range(0,n):
            for j in range(target + 1):
                if j < nums[i]:
                    f[i+1][j] = f[i][j]
                else:
                    f[i + 1][j] = f[i][j] + f[i][j - nums[i]]
        
        return f[-1][-1]