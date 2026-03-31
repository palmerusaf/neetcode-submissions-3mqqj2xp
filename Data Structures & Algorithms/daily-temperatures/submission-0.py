class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=temperatures
        res=[0]*len(n)
        st=[]
        for i in range(len(n)):
            v=n[i]
            while st and v>st[-1][0]:
                _,si=st.pop()
                res[si]=(i-si)
            st.append([v,i])
        return res