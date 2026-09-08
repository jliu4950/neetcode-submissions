class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def if_Palindrome(l,r,s):
            res = True
            while l < r:
                if s[l] != s[r]:
                    res = False
                l += 1
                r -= 1
            return res

        n = len(s)
        path = []
        ans = []
        def dfs(i):
            if i == n:
                ans.append(path[:])
                return 

            for j in range(i,n):
                if if_Palindrome(i,j,s):
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)    
        return ans


        