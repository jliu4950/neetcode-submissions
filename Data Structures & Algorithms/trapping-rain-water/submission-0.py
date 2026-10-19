class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max = 0
        post_max = 0

        n = len(height)

        pre = [0] * n
        post = [0] * n

        for i in range(n):
            if height[i] > pre_max:
                pre_max = height[i]
            pre[i] = pre_max
        
        for i in range(n - 1,-1,-1):
            if height[i] > post_max:
                post_max = height[i]
            post[i] = post_max
        
        res = 0
        for i in range(n):
            res += min(pre[i],post[i]) - height[i]
        
        return res