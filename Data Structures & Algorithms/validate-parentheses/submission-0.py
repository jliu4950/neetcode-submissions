class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')', '{': '}', '[':']'}

        stack=[]

        for c in s:
            if c in dic.values():
                if not stack:
                    return False
                elif dic[stack[-1]] != c:
                    return False
                elif dic[stack[-1]] == c:
                    stack.pop()
            else:
                stack.append(c)
        
        return False if stack else True