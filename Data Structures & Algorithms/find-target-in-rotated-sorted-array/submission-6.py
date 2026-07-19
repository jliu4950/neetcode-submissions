class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<r: #左闭右开
            m=(r-l)//2+l
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<=nums[r]:
                r=m
        
        pivot=l
        
        if target>=nums[pivot] and target<=nums[-1]:
            l=pivot
            r=len(nums)-1
        else:
            l=0
            r=pivot-1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        