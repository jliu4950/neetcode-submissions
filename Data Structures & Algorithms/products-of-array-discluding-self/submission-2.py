class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]*len(nums)

        pre=1
        for i in range(1,len(nums)):
            pre=pre*nums[i-1]
            res[i]=pre
        
        suf=1
        for i in range(len(nums)-2,-1,-1):
            suf=suf*nums[i+1]
            res[i]=res[i]*suf
        
        return res