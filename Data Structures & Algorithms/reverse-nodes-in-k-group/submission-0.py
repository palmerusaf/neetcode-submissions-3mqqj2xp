# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def f(h,k):
            c=h
            g=0
            while c and g<k:
                c=c.next
                g+=1
            
            if g==k:
                c=f(c,k)
                while g>0:
                    t=h.next
                    h.next=c
                    c=h
                    h=t
                    g-=1
                h=c
            return h
        return f(head,k)