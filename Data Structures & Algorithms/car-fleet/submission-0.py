class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[[p,s] for p,s in zip(position,speed)]
        cars.sort(key= lambda x : -x[0])

        st=[] #记录每辆车达到终点的时间

        for p,s in cars:
            # print(st)
            # print((target-p)/s)
            st.append((target-p)/s)
            if len(st)>1 and st[-1]<=st[-2]:
                st.pop()
        
        return len(st)