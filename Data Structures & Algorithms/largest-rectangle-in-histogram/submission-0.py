class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        st=[]
        n=heights

        for i in range(len(n)+1):
            while st and (i==len(n) or n[st[-1]]>=n[i]):
                h=n[st.pop()]
                w=i if not st else i-st[-1]-1
                res=max(res,h*w)
            st.append(i)
        return res