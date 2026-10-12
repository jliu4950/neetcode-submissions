class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r :
            h = min(heights[l],heights[r])
            w = r - l
            maxWater = max(maxWater,h * w)

            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        
        return maxWater