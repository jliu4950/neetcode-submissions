# 维护区间范围内是答案
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r - l)//2 + l
            if nums[m] > nums[r]:
                # min value in [m + 1,r]
                l = m + 1
            else:
                # min value in [l , m]
                r = m
            
        return nums[l]
        