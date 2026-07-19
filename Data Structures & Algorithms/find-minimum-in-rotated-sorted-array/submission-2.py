class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]
        
        l=0
        r=len(nums)-1
        res=nums[-1]
        
        while l<=r:
            m=l+(r-l)//2
            #print(f"[{l}:{r}],{m}")
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<=nums[r]:
                r=m-1
                res=min(res,nums[m])
        
        return res
        