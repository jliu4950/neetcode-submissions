class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(idx):
            if idx == len(nums):
                res.append(path[:])
                return
            
            # 不选
            dfs(idx + 1)

            #选
            path.append(nums[idx])
            dfs(idx + 1)
            path.pop()
        
        dfs(0)
        return res