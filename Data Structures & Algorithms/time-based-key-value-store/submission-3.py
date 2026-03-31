class TimeMap:

    def __init__(self):
        self.r={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        r=self.r
        k,v,t=key,value,timestamp
        if k not in r:r[k]=[]
        r[k].append([t,v])

    def get(self, key: str, timestamp: int) -> str:
        rt=self.r
        k,t=key,timestamp
        if k not in rt:return ''
        n=[t for t,v in rt[k]]
        l,r=0,len(n)-1
        res=l
        while l<=r:
            m=(l+r)//2
            if n[m]<=t:
                res=m
                l=m+1
            else:
                r=m-1
        return rt[k][res][1] if n[res]<=t else ''
