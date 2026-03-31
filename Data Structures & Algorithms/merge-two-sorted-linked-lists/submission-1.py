# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        d=ListNode()
        it=d
        while l1 and l2:
            #do stuff
            if l1.val<=l2.val:
                it.next=l1
                l1=l1.next
            else:
                it.next=l2
                l2=l2.next
            it=it.next
        if l1:
            it.next=l1
        if l2:
            it.next=l2
        return d.next