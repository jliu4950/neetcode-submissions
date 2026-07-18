class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        heights=[0]+heights+[0]
        st=[] # find右边第一个比自己小的，单调递增
        for i,h in enumerate(heights):
            while len(st)>1 and h<st[-1][1]:
                stackInd,stackHt=st.pop()
                w=i-st[-1][0]-1
                res=max(w*stackHt,res)
            st.append([i,h])
        
        return res
        