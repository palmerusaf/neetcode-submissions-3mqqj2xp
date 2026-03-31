class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m={}
        for c in s1:
            m[c]=1+m.get(c,0)
        l=len(s1)
        for i in range(l,len(s2)+1):
            sub=s2[i-l:i]
            lm={}
            for c in sub:
                lm[c]=1+lm.get(c,0)
            if m==lm:
                return True
        return False