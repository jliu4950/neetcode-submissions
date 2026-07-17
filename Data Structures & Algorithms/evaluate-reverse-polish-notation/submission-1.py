class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+', '-', '*', '/']
        st=[]

        for c in tokens:
            if c not in op:
                st.append(c)
            else:
                a=int(st.pop())
                b=int(st.pop())
                answer=0
                if c=="+":
                    answer=a+b
                elif c=="-":
                    answer=b-a
                elif c=="*":
                    answer=a*b
                elif c=="/":
                    answer=b/a
                
                st.append(answer)
        
        return int(st[-1])