class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        l={i:[] for i in range(n)}
        for i,j in edges:
            l[i].append(j)
            l[j].append(i)
        res=[0]
        v=[]
        def f(n,ic=False):
            if n in v:return
            if ic:res[0]+=1
            v.append(n)
            for nn in l[n]:f(nn,)
        for n in l:
            f(n,ic=True)
        return res[0]