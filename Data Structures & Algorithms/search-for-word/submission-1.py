class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w=word
        b=board
        def f(i1,i2,iw=0):
            if iw==len(w):return True
            if i1==len(b) or i2==len(b[i1]):return False
            if i1<0 or i2<0:return False
            if w[iw]!=b[i1][i2]:return False

            iw+=1
            t=b[i1][i2]
            b[i1][i2]='#'
            res= (
                f(i1,i2+1,iw) or
                f(i1,i2-1,iw) or
                f(i1+1,i2,iw) or
                f(i1-1,i2,iw)
            )
            b[i1][i2]=t
            return res
        for i in range(len(b)):
            for j in range(len(b[i])):
                if f(i,j):return True
        return False