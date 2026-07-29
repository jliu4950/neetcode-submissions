import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        
        for num in nums[k:]:
            heapq.heappush(hp,num) # log k
            if len(hp) > k:
                heapq.heappop(hp)
        
        return hp[0]
        