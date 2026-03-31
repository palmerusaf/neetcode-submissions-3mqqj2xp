class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=nums
        dp={}
        def f(l,r,c):
            if l in dp and r in dp[l] and c in dp[l][r]:return dp[l][r][c]
            if l==len(n) or r==len(n):return c
            res=max(f(l+1,r+1,c),f(l,r+1,c),sum(n[l:r+1]))
            if l not in dp:dp[l]={}
            if r not in dp[l]:dp[l][r]={}
            dp[l][r][c]=res
            return res
        return f(0,0,-float('inf'))