class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        l = r = 0

        res = 0
        while r < len(nums):
            if r >= len(nums) - 1:
                break
            for i in range(l,r + 1):
                farthest = max(farthest,nums[i] + i)
            l = r + 1
            r = farthest

            res += 1 

        return res       