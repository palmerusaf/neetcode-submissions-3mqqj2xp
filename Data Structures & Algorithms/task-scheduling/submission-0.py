class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l={}
        for t in tasks:
            l[t]=1+l.get(t,0)
        l=l.values()
        l=list(l)
        heapq.heapify_max(l)
        pu=lambda v:heapq.heappush_max(l,v)
        po=lambda:heapq.heappop_max(l)
        from collections import deque
        q=deque()
        t=0
        while l or q:
            t+=1
            print(q, l)
            v=po()-1 if l else 0
            if v:
                q.append([v,t+n])
            te=q[0][1] if q else -1
            if te==t:
                pu(q.popleft()[0])
        return t

        