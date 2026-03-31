class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def f(t):
            if t==0:return 0
            if t in dp:return dp[t]
            res=float('inf')
            for c in coins:
                if t-c>=0:
                    res=min(res,1+f(t-c))
            dp[t]=res
            return res
        res=f(amount)
        return res if res<float('inf') else -1