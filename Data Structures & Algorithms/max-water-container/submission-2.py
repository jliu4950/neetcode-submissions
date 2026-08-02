class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            h = min(heights[l],heights[r])
            w = r - l
            res = max(res,h * w)

            if heights[l] <= heights[r]:
                left_h=heights[l]
                # l = r-1
                while l < r and heights[l+1] < left_h:
                    l = l + 1
                l = l + 1
            else:
                right_h = heights[r]
                while l < r and heights[r-1] < right_h:
                    r= r- 1
                r = r - 1
        
        return res

        