class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        speed + hours -
        find left boundary 
        [......|......]
                left part :less than h
               l
              r
        '''
        l = 1
        r = max(piles)

        while l <= r:
            k = (r - l) // 2 + l
            hour = 0
            for p in piles:
                hour += (p + k - 1) // k
            #print(k,hour)
            if hour <= h:
                r = k - 1
            else:
                l = k + 1
        return l

'''
红蓝染色法：
1. 单调递增的数组，找到>= target 的位置
[2,4,5,6,8,9] target = 7
         l
       r  
保证l及其右边都是>= target的
保证r及其左边都是< target 的

2. > target:
保证l及其右边都是> target的
保证r及其左边都是<= target 的

3. <=
'''

