class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=['']
        def p(l,r):
            if l<0 or r>len(s)-1:return
            if s[l]!=s[r]:return
            w=s[l:r+1]
            if len(w)>len(res[0]):res[0]=w
            p(l-1,r+1)
        for i in range(len(s)):
            p(i,i+1)
            p(i,i)
        return res[0]