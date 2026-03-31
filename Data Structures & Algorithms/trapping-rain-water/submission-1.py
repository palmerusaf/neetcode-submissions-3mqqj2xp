class Solution:
    def trap(self, height: List[int]) -> int:
        n=height
        l=[0]*len(n)
        r=[0]*len(n)
        for i in range(1,len(n)):
            l[i]=max(l[i-1],n[i-1])
        for i in range(len(n)-2,-1,-1):
            r[i]=max(r[i+1],n[i+1])
        m=[min(li,ri) for li,ri in zip(l,r)]
        print(l,r,m)
        return sum([max(0,mi-h) for mi,h in zip(m,n)])