class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        p=prerequisites
        l={i[0]:[] for i in p}
        for i in p:
            l[i[0]].append(i[1])
        def f(n,v):
            if n not in l:return True
            if n in v:return False
            v.append(n)
            for nn in l[n]:
                if not f(nn,v[:]):return False
            return True
        for i in p:
            if not f(i[0],[]):return False
        return True