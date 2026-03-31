class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        r=n()
        b=board
        for w in words:r.a(w)
        res=[]
        def f(r,i,j,w):
            if i==-1 or j ==-1 or i==len(b) or j==len(b[0]):return
            c=b[i][j]
            if not r or c not in r.c:return
            r=r.c[c]
            w+=c
            if r.e and w not in res:res.append(w)
            b[i][j]=''
            f(r,i,j+1,w)
            f(r,i,j-1,w)
            f(r,i+1,j,w)
            f(r,i-1,j,w)
            b[i][j]=c

        for i in range(len(b)):
            for j in range(len(b[i])):
                f(r,i,j,'')
        return res

class n:
    def __init__(self):
        self.e=False
        self.c={}
    def a(self,w):
        it=self
        for c in w:
            if c not in it.c:it.c[c]=n()
            it=it.c[c]
        it.e=True