class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(p,s) for p,s in zip(position,speed)]
        car.sort(key = lambda x: -x[0])

        st = []

        for p,s in car:
            t = (target - p) / s
            if st and t <= st[-1]:
                continue
            else:
                st.append(t)
        return len(st)