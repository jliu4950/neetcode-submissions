class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f0,f1 = 0,0
        for i in range(n - 1,- 1,- 1):
            f = cost[i] + min(f0,f1)
            f0,f1 = f1,f

        from_0 = f1
        f0,f1 = 0,0
        for i in range(n - 1,0,-1):
            f = cost[i] + min(f0,f1)
            f0,f1 = f1,f
        from_1 = f1

        return min(from_0,from_1)