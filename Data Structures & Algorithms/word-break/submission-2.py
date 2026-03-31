class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        def f(i):
            if i in dp:return dp[i]
            if i ==len(s):return True

            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    if f(i+len(w)):
                        dp[i]=True
                        return True
            dp[i]=False
            return False
        return f(0)