"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m={}
        def f(n):
            if n in m:return m[n]
            if not n:return None
            c=Node(val=n.val)
            m[n]=c
            for nn in n.neighbors:
                c.neighbors.append(f(nn))
            return c
        return f(node)
