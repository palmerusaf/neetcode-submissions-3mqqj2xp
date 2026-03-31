class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={v:0 for v in nums}
        for v in nums:
            res[v]+=1
        res=sorted(res.items(),key=lambda i:i[1])
        res=res[::-1]
        res=[x[0] for x in res][:k]
        return res
