class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'|'+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            il=''
            while(s[i]!='|'):
                il+=s[i]
                i+=1
            il=int(il)
            i+=1
            v=s[i:i+il]
            print(v)
            res.append(v)
            i=i+il
        print(res)
        return res