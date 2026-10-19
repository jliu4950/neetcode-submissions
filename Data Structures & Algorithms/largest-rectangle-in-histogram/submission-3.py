class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #record leftmax and rightmax
        maxArea = 0
        st = []

        for i,h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                stIdx,stH = st.pop()
                maxArea = max(maxArea,(i - stIdx)*stH)
                start = stIdx
            st.append((start,h))
        
        for i,cur in enumerate(st):
            maxArea = max(maxArea,cur[1] * (len(heights) - cur[0]))
        return maxArea