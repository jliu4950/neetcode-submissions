class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<r: #左闭右开
            m=(r-l)//2+l
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<=nums[r]:
                r=m
        
        return nums[l]
        