class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 问最大、最小、能不能，用greedy
        farest = 0 # i之前能到达的最远距离是什么？
        for i,num in enumerate(nums):
            if i > farest:
                return False
            else:
                farest = max(farest , nums[i] + i)
        
        return True