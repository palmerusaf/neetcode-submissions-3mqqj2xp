class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=stones
        hq=heapq
        po=lambda :hq.heappop_max(s)
        hq.heapify_max(s)
        pu=lambda v:hq.heappush_max(s,v)
        while len(s)>1:
            pu(abs(po()-po()))
        return s[0]