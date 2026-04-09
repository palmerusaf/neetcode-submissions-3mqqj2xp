class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m=defaultdict(list)
        for a,b in sorted(tickets,key=lambda i:i[1]):
            m[a].append(b)
        res=['JFK']
        def f(a):
            if len(res)==len(tickets)+1:return True
            if a not in m:return False

            t=m[a][:]
            for i,b in enumerate(t):
                m[a].pop(i)
                res.append(b)

                if f(b):return True
                m[a].insert(i,b)
                res.pop()
            return False
        f('JFK')
        return res