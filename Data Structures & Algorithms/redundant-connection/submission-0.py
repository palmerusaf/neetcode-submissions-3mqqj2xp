class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e=edges
        m={}
        v=set()
        def f(n,p):
            if n in v:
                return True
            v.add(n)
            for nn in m[n]:
                if nn==p:
                    continue
                if f(nn,n):
                    return True
            v.remove(n)
            return False
        for a,b in e:
            if not a in m:
                m[a]=set()
            if not b in m:
                m[b]=set()
            m[a].add(b)
            m[b].add(a)
            if f(a,-1):
                return [a,b]
            
