class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        l=stones
        while len(l)>1:
            f=heapq.heappop_max(l)
            s=heapq.heappop_max(l)
            if f>s:
                heapq.heappush_max(l,f-s)
        return 0 if not l else l[0]