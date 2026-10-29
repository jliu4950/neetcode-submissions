class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        end = 0

        res = 0
        i = 0
        while i < len(nums):
            if end >= len(nums) - 1:
                break
            while i <= end:
                farthest = max(i + nums[i],farthest)
                i += 1
            end = farthest
            res += 1
        
        return res
            
