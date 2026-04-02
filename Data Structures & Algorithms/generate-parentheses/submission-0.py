class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st=[]
        res=[]
        def f(on,cn):
            if on==cn==n:
                res.append(''.join(st))
                return
            if on<n:
                st.append('(')
                f(on+1,cn)
                st.pop()
            if cn<on:
                st.append(')')
                f(on,cn+1)
                st.pop()
        f(0,0)
        return res