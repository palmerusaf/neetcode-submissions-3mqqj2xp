class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def f(t):
            if t in dp:return dp[t]
            if t==n:return 1
            if t>n:return 0
            res=f(t+1)+f(t+2)
            dp[t]=res
            return res
        return f(0)