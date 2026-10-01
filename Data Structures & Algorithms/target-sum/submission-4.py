class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = target + sum(nums)
        
        if target < 0 or target % 2:
            return 0 
        
        target = target // 2

        n = len(nums)

        f = [0] * (target + 1)
        f[0] = 1
        
        for i in range(n):
            for c in range(target,-1,-1):
                if c >= nums[i]:
                    f[c] = f[c] + f[c - nums[i]]
        return f[-1]
        # f = [[0] * (target + 1) for _ in range(2)] #只需要两行
        # f[0][0] = 1 # 初始化

        # for i in range(0,n):
        #     for j in range(target+1,0,-1):
        #         if j < nums[i]:
        #             f[(i+1)%2][j] = f[i%2][j]
        #         else:
        #             f[(i+1)%2][j] = f[i%2][j] + f[i%2][j - nums[i]]
        
        return f[-1][-1]