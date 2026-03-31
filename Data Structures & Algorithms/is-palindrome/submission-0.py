import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        false=False
        true=True
        s=re.sub(r'\W+','',s.upper())
        l=0
        r=len(s)-1
        while(l<r):
            if(s[l]!=s[r]):
                return false
            l+=1
            r-=1
        return true
        