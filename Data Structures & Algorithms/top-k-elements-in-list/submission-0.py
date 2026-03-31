class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            d[n]=d[n]+1 if n in d else 1
        sd=sorted(d.items(),key=lambda x:x[1])[::-1]
        return [i for i,_ in sd[:k]]