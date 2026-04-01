class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        pu=lambda v:heapq.heappush(h,v)
        po=lambda:heapq.heappop(h)
        for n in nums:
            pu(n)
            if len(h)>k:
                po()
        return h[0]