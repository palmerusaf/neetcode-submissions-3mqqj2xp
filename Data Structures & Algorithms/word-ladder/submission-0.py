class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ew=endWord
        bw=beginWord
        wl=wordList
        if ew not in wl:return 0
        n=collections.defaultdict(list)
        wl.append(bw)
        for w in wl:
            for j in range(len(w)):
                p=w[:j]+'*'+w[j+1:]
                n[p].append(w)
        
        v=set()
        v.add(bw)
        res=1
        q=deque()
        q.append(bw)

        while q:
            for i in range(len(q)):
                w=q.popleft()
                if w==ew:return res
                for j in range(len(w)):
                    p=w[:j]+'*'+w[j+1:]
                    for nw in n[p]:
                        if nw not in v:
                            v.add(nw)
                            q.append(nw)
            res+=1
        return 0