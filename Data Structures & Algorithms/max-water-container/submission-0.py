class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=0
        for i,left in enumerate(heights):
            for j in range(i+1,len(heights)):
                h=min(left,heights[j])
                w=j-i
                water=max(water,h*w)
        
        return water
        