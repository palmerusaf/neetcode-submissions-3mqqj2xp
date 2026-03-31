class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={
            '+':lambda a,b:a+b,
            '/':lambda a,b:int(a/b),
            '*':lambda a,b:a*b,
            '-':lambda a,b:a-b
        }
        st=[]
        for c in tokens:
            if c in op.keys():
                b=st.pop()
                a=st.pop()
                st.append(op[c](a,b))
            else:
                st.append(int(c))
        return st[-1]