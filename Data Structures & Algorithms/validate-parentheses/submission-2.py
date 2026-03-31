class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        ob='([{'
        cb=')]}'
        for c in s:
            if c in ob:
                st.append(c)
            if c in cb:
                if len(st)>0 and ob.index(st[-1]) == cb.index(c):
                    st.pop()
                else:
                    return False
        return len(st)==0