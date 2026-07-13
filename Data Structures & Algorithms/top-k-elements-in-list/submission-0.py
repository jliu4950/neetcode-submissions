import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        
        hp=[]
        for num,freq in dic.items():
            heapq.heappush(hp,(freq,num))
        
        for i in range(len(dic)-k):
            heapq.heappop(hp)
        
        res=[i[1] for i in hp]

        return res
        