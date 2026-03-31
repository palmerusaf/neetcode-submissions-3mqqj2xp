# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def f(r):
            if not r:return 0
            lm,rm=max(f(r.left),0),max(f(r.right),0)
            nosp=r.val+lm+rm
            res[0]=max(res[0],nosp)
            sp=r.val+max(lm,rm)
            return sp
        f(root)
        return res[0]