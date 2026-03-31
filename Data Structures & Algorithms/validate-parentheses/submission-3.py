class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        ob='([{'
        cb=')]}'
        for c in s:
            if c in ob:
                st.append(c)
            if c in cb:
                if st and ob.index(st[-1]) == cb.index(c):
                    st.pop()
                else:
                    return False
        return not st