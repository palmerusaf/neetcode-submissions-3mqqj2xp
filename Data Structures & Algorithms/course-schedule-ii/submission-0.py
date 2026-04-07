class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        p=prerequisites
        g={}
        v=set()
        c=set()
        res=[]
        for a,b in p:
            if a not in g:
                g[a]=[]
            g[a].append(b)
        def f(nd):
            if nd in c:
                return False
            if nd in v:
                return True
            c.add(nd)
            for pr in g.get(nd,[]):
                if not f(pr):
                    return False
            c.remove(nd)
            v.add(nd)
            res.append(nd)
            return True
        for i in range(n):
            if not f(i):
                return []
        return res