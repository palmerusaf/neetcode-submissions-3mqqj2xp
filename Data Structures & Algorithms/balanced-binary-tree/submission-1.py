# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ib=self.isBalanced
        def h(root):
            return 0 if not root else 1 + max(h(root.left),h(root.right))
        if not root:
            return True
        if abs(h(root.left)-h(root.right))>1:
            return False
        return ib(root.left) and ib(root.right)
        