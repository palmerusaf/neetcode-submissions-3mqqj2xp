class Twitter:

    def __init__(self):
        self.c=0
        self.m={}
        self.f={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        k,v=userId,tweetId
        if k not in self.m:self.m[k]=[]
        self.m[k].append([self.c,v])
        self.c+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        k=userId
        if k not in self.f:self.f[k]=set()
        self.f[k].add(k)
        for k in self.f.get(userId):
            for i in self.m.get(k,[]):
                res.append(i)
        res.sort(key=lambda i:-i[0])
        res=[i[1] for i in res][:10]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        k,v=followerId,followeeId
        if k not in self.f:self.f[k]=set([k])
        self.f[k].add(v)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        k,v=followerId,followeeId
        if k not in self.f:self.f[k]=set([k])
        if v in self.f[k]:self.f[k].remove(v)
