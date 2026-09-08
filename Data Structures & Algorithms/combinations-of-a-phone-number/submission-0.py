class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        n = len(digits)

        if n == 0:
            return []
            
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            
            for char in dic[int(digits[i])]:
                path.append(char)
                dfs(i + 1)
                path.pop()
            
        dfs(0)
        return ans