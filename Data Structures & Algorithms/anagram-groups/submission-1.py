class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def an(a,b):
            return sorted(a)==sorted(b)
        res=[]
        for s in strs:
            paired=False
            for i in range(len(res)):
                if an(s,res[i][0]):
                    res[i].append(s)
                    paired=True
            if not paired:
                res.append([s])
        return res