class Solution:
    def rob(self, nums: List[int]) -> int:
        f0,f1 = 0,0
        n = len(nums)

        for i in range(n):
            f = max(f1,f0 + nums[i])
            f0,f1 = f1,f
        
        return f1