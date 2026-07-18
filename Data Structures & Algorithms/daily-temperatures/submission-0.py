class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[] #pair: [val,index]
        res=[0]*len(temperatures)

        for i,tp in enumerate(temperatures):
            while st and tp>st[-1][0]:
                stackTp,stackIn=st.pop()
                res[stackIn]=i-stackIn
            
            st.append([tp,i])
        
        return res