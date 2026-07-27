import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.hp = []

        for num in nums:
            heapq.heappush(self.hp,num)
        
        if len(nums)>k:
            for _ in range(len(nums)-k):
                heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heappush(self.hp,val)
        if len(self.hp) == self.k:
            return self.hp[0]

        heapq.heappop(self.hp)
        return self.hp[0]
#[3]
        
