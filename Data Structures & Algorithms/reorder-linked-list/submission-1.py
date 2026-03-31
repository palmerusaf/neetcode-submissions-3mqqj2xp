# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        def p(h):
            s=[]
            while h:
                s.append(h.val)
                h=h.next
            print(s)
        f,s=head,head
        pr=s
        while f and f.next:
            f=f.next.next
            pr=s
            s=s.next
        pr.next=None
        def r(h):
            pr,c=None,h
            while c:
                t=c.next
                c.next=pr
                pr=c
                c=t
            return pr
        s=r(s)
        l1,l2=head,s
        p(l1)
        p(l2)
        while l1 or l2:
            if not l1.next:
                l1.next=l2
                break
            t1,t2=l1.next,l2.next
            l1.next=l2
            l2.next=t1
            l1,l2=t1,t2
        p(head)
