class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        n=nums
        def f(i):
            if i>=len(n):return 0
            res=max(f(i+1),nums[i]+f(i+2)) if i not in dp else dp[i]
            dp[i]=res
            return res
        return f(0)