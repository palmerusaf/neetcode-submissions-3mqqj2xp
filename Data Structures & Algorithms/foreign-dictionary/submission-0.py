class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        l={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minL=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minL]==w2[:minL]:
                return ''
            for j in range(minL):
                if w1[j]!=w2[j]:
                    l[w1[j]].add(w2[j])
                    break
        v={}
        res=[]
        def f(c):
            if c in v:
                return v[c]
            
            v[c]=True
            for nc in l[c]:
                if f(nc):
                    return True
            
            v[c]=False
            res.append(c)
        for c in l:
            if f(c):return''
        return ''.join(res[::-1])