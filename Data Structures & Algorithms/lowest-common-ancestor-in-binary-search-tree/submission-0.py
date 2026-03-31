# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca=root
        l=min(p.val,q.val)
        h=max(p.val,q.val)
        while not l<lca.val<h:
            if l>lca.val:
                lca=lca.right
            elif h<lca.val:
                lca=lca.left
            else:
                break
        return lca
