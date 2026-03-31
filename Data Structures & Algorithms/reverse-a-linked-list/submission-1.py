# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pr,it=None,head
        while it:
            t=it.next
            it.next=pr
            pr=it
            it=t
        return pr