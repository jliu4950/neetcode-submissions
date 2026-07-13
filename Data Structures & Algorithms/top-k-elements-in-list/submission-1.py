import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1

        f=[[] for _ in range(len(nums)+1)]

        for num,freq in dic.items():
            f[freq].append(num)
        
        res=[]
        
        count=1

        for i in range(len(f)-1,0,-1):
            if count>k:
                break
            for num in f[i]:
                res.append(num)
                count+=1

        return res
        