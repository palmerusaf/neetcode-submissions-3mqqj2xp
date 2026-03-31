class PrefixTree:
    class n:
        def __init__(self):
            self.e=False
            self.c={}
        
    def __init__(self):
        self.r=self.n()

    def insert(self, word: str) -> None:
        w=word
        it=self.r
        for c in w:
            if c not in it.c:
                it.c[c]=self.n()
            it=it.c[c]
        it.e=True

    def search(self, word: str) -> bool:
        it=self.r
        for c in word:
            if c not in it.c:
                return False
            it=it.c[c]
        return it.e        

    def startsWith(self, prefix: str) -> bool:
        it=self.r
        for c in prefix:
            if c not in it.c:
                return False
            it=it.c[c]
        return True