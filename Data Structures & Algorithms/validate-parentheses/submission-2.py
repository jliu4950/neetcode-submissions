class Solution:
    def isValid(self, s: str) -> bool:
        '''
        st : [](){}
        ([{}])
        [(])
        1.[(] 左右括号不match false
        2.none ] false
        3.[   全部走完了，还有剩下的 false
        else true
        '''
        st = []
        dic = {"]":"[","}":"{",")":"("}

        for char in s:
            if char in dic.values():
                st.append(char)
            elif char in dic:
                if st and dic[char] == st[-1]:
                    st.pop()
                else:
                    return False
        
        return True if not st else False