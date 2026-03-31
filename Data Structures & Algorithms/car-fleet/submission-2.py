class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps=[[p,s] for p,s in zip(position,speed)]
        ps.sort()
        ps=ps[::-1]
        t=target
        ttt=[(t-p)/s for p,s in ps]
        res=1
        print(ttt)
        l=ttt[0]
        for i in range(1,len(ttt)):
            r=ttt[i]
            if r>l:
                res+=1
                l=r
        return res