class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        for i in range(len(heights)):
            minHeights=[i,heights[i]] 
            res=max(heights[i],res)
            for j in range(i,len(heights)):
                if heights[j]<minHeights[1]:
                    minHeights[0]=j
                    minHeights[1]=heights[j]
                
                area=(j-i+1)*minHeights[1]
                res=max(area,res)
        
        return res
        