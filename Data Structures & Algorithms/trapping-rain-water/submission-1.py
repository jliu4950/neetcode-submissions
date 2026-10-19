class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        pre = 0
        post = 0

        res = 0
        while l <= r:
            pre = max(height[l],pre)
            post = max(height[r],post)
            if pre <= post:
                res += pre - height[l]
                l += 1
            else:
                res += post - height[r]
                r -= 1
        
        return res