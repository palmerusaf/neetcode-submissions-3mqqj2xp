class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        res=0
        if len(s)==1:
            return 1
        while r<len(s):
            while len(s[l:r+1])!=len(set(s[l:r+1])):
                l+=1
            r+=1
            res=max(res,r-l)
        return res