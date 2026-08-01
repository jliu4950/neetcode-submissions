class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(idx,sums):
            if sums == target:
                res.append(path.copy())
                return
            elif sums > target :
                return
            
            for i in range(idx,len(nums)):
                if sums + nums[i] > target:
                    break
                path.append(nums[i])
                sums += nums[i]
                dfs(i,sums)
                sums -= nums[i]
                path.pop()
        
        dfs(0,0)

        return res