class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 0
        f1 = 1

        for i in range(n):
            f = f0 + f1
            f0,f1 = f1,f
        return f1

'''
1,2,3,4,5
1,
'''