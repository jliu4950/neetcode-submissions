class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path,i,sums):
            if sums == target:
                res.append(path[:])
                return
            elif sums > target:
                return
            if i == len(nums):
                return

            dfs(path+[nums[i]],i,sums+nums[i])

            dfs(path,i+1,sums)
        
        dfs([],0,0)
        return res
        