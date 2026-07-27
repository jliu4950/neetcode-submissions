import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        hp = []

        for num in self.nums:
            heapq.heappush(hp,num)
        
        for _ in range(len(self.nums)-self.k):
            heapq.heappop(hp)
        return heapq.heappop(hp)

        
