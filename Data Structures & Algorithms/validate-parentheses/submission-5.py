class Solution:
    def isValid(self, s: str) -> bool:
        bt={
            "{":"}",
            "(":")",
            "[":"]"
        }
        st=[]
        for c in s:
            if c in bt.keys():
                st.append(c)
            if c in bt.values():
                if len(st) and bt[st[-1]]==c:
                    st.pop()
                else:
                    return False
        return not len(st)