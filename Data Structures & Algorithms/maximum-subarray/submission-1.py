class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = nums[0]

        s = 0
        for i,num in enumerate(nums):
            if s < 0:
                s = 0
            if s + num > 0:
                s += num
            else:
                s = num
            res = max(s,res)
        
        return res