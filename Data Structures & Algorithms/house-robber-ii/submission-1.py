class Solution:
    def rob(self, nums: List[int]) -> int:
        def steal_from(start,end):
            f0,f1 = 0,0
            for i in range(start,end):
                f = max(f0 + nums[i],f1)
                #print(start,end,f)
                f0,f1 = f1,f
            
            return f1
        if len(nums) == 1:
            return nums[0]
            
        return max(steal_from(0,len(nums) - 1),steal_from(1,len(nums)))
            