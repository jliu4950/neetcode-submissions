class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] 
        path = []
        
        def backtracking(nums,start):
            if start == len(nums)-1:
                path.append(nums[-1])
                res.append(path[:])
                path.pop()
                return

            for i in range(start,len(nums)):
                path.append(nums[i])
                res.append(path[:])
                backtracking(nums,i+1)
                path.pop()
        
        backtracking(nums,0)
        return res
        