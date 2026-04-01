class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.m=OrderedDict()
        self.c=capacity

    def get(self, key: int) -> int:
        m=self.m
        if key not in m:return -1
        m.move_to_end(key)
        return m[key]

    def put(self, key: int, value: int) -> None:
        m=self.m
        c=self.c
        m[key]=value
        m.move_to_end(key)
        if len(m)>c:
            m.popitem(last=False)

