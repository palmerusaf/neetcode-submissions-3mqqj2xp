# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def f(r=root,pr=-float('inf')):
            nonlocal res
            if not r:return
            if pr<=r.val:
                res+=1
            pr=max(pr,r.val)
            f(r.left,pr)
            f(r.right,pr)
        f()
        return res