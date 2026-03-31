# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def s(r,sr):
            if not r and not sr:return True
            if not r or not sr:return False
            return r.val==sr.val and s(r.left,sr.left) and s(r.right,sr.right)
        r,sr=root,subRoot
        if not r:return False
        ss=self.isSubtree
        return s(r,sr) or ss(r.left,sr) or ss(r.right,sr)