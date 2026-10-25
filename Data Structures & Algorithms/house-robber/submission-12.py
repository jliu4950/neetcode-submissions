class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i,x in enumerate(nums):
            dp[i + 2] = max(dp[i + 1],dp[i] + nums[i])
        
        return dp[-1]
