# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st=self.isSameTree

        if not p and not q:return True
        if not p or not q:return False

        return p.val==q.val and st(p.left,q.left) and st(p.right,q.right)