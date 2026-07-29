import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []

        for stone in stones:
            heapq.heappush(hp,- stone)
        
        while len(hp) > 1 :
            fst = heapq.heappop(hp)
            scd = heapq.heappop(hp)
            if fst != scd:
                heapq.heappush(hp, fst - scd)
        return - hp[0] if hp else 0