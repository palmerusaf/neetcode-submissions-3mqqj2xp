class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        l=[]
        r=[]
        b=heights
        def f(i,j,l,ph=-float('inf')):
            if [i,j] in l or i<0 or j<0 or i==len(b) or j==len(b[0]):return
            ch=b[i][j]
            if ch<ph:return
            l.append([i,j])
            f(i,j+1,l,ch)
            f(i,j-1,l,ch)
            f(i+1,j,l,ch)
            f(i-1,j,l,ch)
        
        for i in range(len(b)):
            f(i,len(b[i])-1,r)
            f(i,0,l)
        for j in range(len(b[0])):
            f(0,j,l)
            f(len(b)-1,j,r)
        for li in l:
            if li in r:
                res.append(li)
        return res