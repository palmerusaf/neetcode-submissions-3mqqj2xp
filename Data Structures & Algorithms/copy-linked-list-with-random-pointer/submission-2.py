"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c=head
        m={}
        while c:
            m[c]=Node(0)
            c=c.next
        c=head
        while c:
            m[c].val=c.val
            m[c].next=m[c.next] if c.next in m else None
            m[c].random=m[c.random] if c.random in m else None
            c=c.next
        return m[head] if head in m else None