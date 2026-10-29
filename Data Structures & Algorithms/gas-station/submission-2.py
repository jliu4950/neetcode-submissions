class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        1, 2, 3, 4
        2, 2, 4, 1
        -1,0,-1, 3
        '''
        
        rest = []
        n = len(gas)

        s = 0
        for i in range(n):
            rest.append(gas[i] - cost[i]) # 从i走到下一站还剩多少汽油
            s += gas[i] - cost[i]
        if s < 0:
            return -1

        start = 0  # 从什么地方出发

        tank = 0 # [start : i + 1] 时油箱里面还有多少油
        for i in range(n):
            tank += rest[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
            
                