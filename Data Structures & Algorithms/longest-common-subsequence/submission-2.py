class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a,b=text1,text2
        dp={}
        def f(ai,bi,c):
            if ai in dp and bi in dp[ai] and c in dp[ai][bi]:return dp[ai][bi][c]
            if ai==len(a) or bi==len(b):return c
            res=f(ai+1,bi+1,c+1)  if a[ai]==b[bi] else max(f(ai+1,bi,c),f(ai,bi+1,c))
            if ai not in dp:dp[ai]={}
            if bi not in dp[ai]:dp[ai][bi]={}
            dp[ai][bi][c]=res
            return res
        return f(0,0,0)