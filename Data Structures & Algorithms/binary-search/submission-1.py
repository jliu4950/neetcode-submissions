class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = ( r - l) // 2 + l
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m + 1
        
        return -1