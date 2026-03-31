# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        r=root
        if not r:return True
        v=self.isValidBST
        def lt(n,t):
            if not n:return True
            if n.val>=t:return False
            return lt(n.left,t) and lt(n.right,t)
        def gt(n,t):
            if not n:return True
            if n.val<=t:return False
            return gt(n.right,t) and gt(n.left,t)
        return lt(r.left,r.val) and gt(r.right,r.val) and v(r.left) and v(r.right)