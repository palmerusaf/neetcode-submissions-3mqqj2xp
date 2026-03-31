# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p,i=preorder,inorder
        if not p or not i:return None
        f=self.buildTree
        val=p[0]
        del p[0]
        m=inorder.index(val)
        return TreeNode(val,left=f(p,i[:m]),right=f(p,i[m+1:]))