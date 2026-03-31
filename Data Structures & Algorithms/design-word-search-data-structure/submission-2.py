class WordDictionary:

    def __init__(self):
        self.r=n()
        

    def addWord(self, word: str) -> None:
        it=self.r
        for c in word:
            if not c in it.c:
                it.c[c]=n()
            it=it.c[c]
        it.e=True

    def search(self, word: str) -> bool:
        def f(r,w):
            if r and not w:return r.e
            if w[0] in r.c:return f(r.c[w[0]],w[1:])
            if w[0]=='.':
                for c in r.c:
                    if f(r.c[c],w[1:]):return True
            return False
        return f(self.r,word)
        
class n:
   def __init__(self):
        self.c={}
        self.e=False