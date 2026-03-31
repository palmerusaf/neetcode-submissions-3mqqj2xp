class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAna(x,y):
            return sorted(x)==sorted(y)
        res=[[strs[0]]]
        for i in range(1,len(strs)):
            s=strs[i]
            mat=False
            for r in res:
                if isAna(r[0],s):
                    r.append(s)
                    mat=True
            if not mat:
                res.append([s])
        return res