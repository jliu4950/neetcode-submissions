class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] 
        path = []
        
        def backtracking(start):
            for i in range(start,len(nums)):
                path.append(nums[i])
                res.append(path[:])
                backtracking(i+1)
                path.pop()
        
        backtracking(0)
        return res
        