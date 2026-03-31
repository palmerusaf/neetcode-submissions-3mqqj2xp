class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=[0]
        g=grid
        def f(i,j):
            if i==-1 or j==-1 or i==len(g) or j==len(g[0]) or g[i][j]=='0':return
            g[i][j]='0'
            f(i,j+1)
            f(i,j-1)
            f(i+1,j)
            f(i-1,j)
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j]=='1':
                    res[0]+=1
                    f(i,j)
        return res[0]
            