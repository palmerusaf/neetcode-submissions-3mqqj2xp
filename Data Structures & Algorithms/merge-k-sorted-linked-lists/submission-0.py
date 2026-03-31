# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ls=lists
        if not ls or not len(ls):return None
        for i in range(1,len(lists)):
            lists[i]=self.ml(lists[i-1],lists[i])
        return lists[-1]
    def ml(self,l1,l2):
        d=ListNode()
        c=d
        while l1 and l2:
            if l1.val<l2.val:
                c.next=l1
                l1=l1.next
            else:
                c.next=l2
                l2=l2.next
            c=c.next
        if l1:
            c.next=l1
        if l2:
            c.next=l2
        return d.next
