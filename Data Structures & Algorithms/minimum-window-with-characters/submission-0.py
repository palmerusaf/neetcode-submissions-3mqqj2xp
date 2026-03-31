class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct,wt={},{}
        for c in t:
            ct[c]=1+ct.get(c,0)
        res=""
        fil,req=0,len(ct)
        rl=float('infinity')
        l=0 
        for r in range(len(s)):
            c=s[r]
            wt[c]=1+wt.get(c,0)

            if c in ct and wt[c]==ct[c]:
                fil+=1
            
            while fil==req:
                if (r-l+1)<rl:
                    res=s[l:r+1]
                    rl=r-l+1
                wt[s[l]]-=1
                if s[l] in ct and wt[s[l]]<ct[s[l]]:
                    fil-=1
                l+=1
        return res