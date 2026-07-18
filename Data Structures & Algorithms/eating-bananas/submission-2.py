import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r

        while l<=r:
            k=(r-l)//2+l
            count=0
            for pile in piles:
                #print(f"{pile//k+1}")
                count+=math.ceil(pile/k)
                #print(f"---{count}------")
            
            if count>h: #如果用时更长
                l=k+1   #增加吃的速度
            elif count<=h: #如果用时更短
                res=min(res,k)
                r=k-1
        return res