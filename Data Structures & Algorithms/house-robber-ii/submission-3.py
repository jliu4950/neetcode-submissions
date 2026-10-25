class Solution:
    def rob(self, nums: List[int]) -> int:

        def build(array):
            f0 = 0 
            f1 = 0

            for i,money in enumerate(array):
                f = max(f0 + money,f1)
                f0,f1 = f1,f

            return f1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(build(nums[1:]),build(nums[:-1]))
        