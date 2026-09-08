class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()
        n = len(nums)

        def dfs(i):
            ans.append(path[:])
            if i == n:
                return 
            
            for j in range(i,n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
            
        dfs(0)
        return ans
        