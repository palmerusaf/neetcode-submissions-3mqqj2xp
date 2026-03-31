class Solution:
    def countSubstrings(self, s: str) -> int:
        res=[0]
        def f(l,r):
            if l<0 or r>len(s)-1 or s[l]!=s[r]:return
            res[0]+=1
            f(l-1,r+1)
        for i in range(len(s)):
            f(i,i)
            f(i,i+1)
        return res[0]