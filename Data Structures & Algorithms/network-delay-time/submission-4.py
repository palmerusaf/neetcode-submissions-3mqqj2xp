class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        e=times
        m=defaultdict(list)
        q=[]
        for a,b,t in e:
            m[a].append([b,t])
        res=0
        q.append([0,k])
        v=set()
        while q:
            ct,a=heapq.heappop(q)
            if a in v:continue
            v.add(a)
            res=max(res,ct)
            for b,t in m[a]:
                if b in v:continue
                heapq.heappush(q,[ct+t,b])
            if len(v)==n:
                break
        return res if len(v)==n else -1