# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=-1
        self.k=k
        def d(r):
            if not r:return
            d(r.left)
            self.k-=1
            if not self.k:self.res=r.val
            d(r.right)
        d(root)
        return self.res