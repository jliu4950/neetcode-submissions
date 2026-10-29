class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        [2,5,6]
        [1,4,4]
        [5,7,5]
        '''

        res = [-1,-1,-1]

        for x,y,z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            else:
                if x == target[0]:res[0] = x
                if y == target[1]:res[1] = y 
                if z == target[2]:res[2] = z 
        
        
        return True if res == target else False
        