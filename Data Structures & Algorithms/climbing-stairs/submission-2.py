class Solution:
    dp={}
    def climbStairs(self, n: int) -> int:
        dp=self.dp
        if n == 0:
            return 1
        if n<0:
            return 0
        if n in dp:
            return dp[n]
        dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return dp[n]