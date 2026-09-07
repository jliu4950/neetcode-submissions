class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [""] * 2 * n

        def dfs(i,open):
            if i == 2 * n:
                ans.append("".join(path))
                return
            
            #choose
            if open < n:
                path[i] = "("
                dfs(i + 1, open + 1)
            
            #not choose
            if i - open < open:
                path[i] = ")"
                dfs(i + 1, open)
        
        dfs(0,0)
        return ans   