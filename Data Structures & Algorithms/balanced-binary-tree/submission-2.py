# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res=True
        def f(rt):
            nonlocal res
            if not res:return 0
            if not rt:return 0
            lh=1+f(rt.left)
            rh=1+f(rt.right)
            res=res and abs(lh-rh)<2
            return max(lh,rh)
        f(root)
        return res