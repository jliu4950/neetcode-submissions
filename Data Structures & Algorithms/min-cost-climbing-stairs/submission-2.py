class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0,f1 = 0,cost[0]
        for i in range(1,len(cost)):
            f = min(f0,f1) + cost[i]
            f0,f1 = f1,f
        
        return min(f0,f1)
        