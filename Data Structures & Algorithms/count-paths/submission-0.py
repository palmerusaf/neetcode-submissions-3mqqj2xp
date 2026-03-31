class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i,j):
            if i==m-1 and j==n-1:return 1
            if i>m-1 or j>n-1:return 0
            return f(i+1,j)+f(i,j+1)
        return f(0,0)