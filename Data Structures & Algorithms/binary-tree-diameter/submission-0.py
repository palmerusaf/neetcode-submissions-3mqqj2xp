# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dbt=self.diameterOfBinaryTree  
        def dfs(n,root):
            return 0 if not root else 1 + max(dfs(n,root.left),dfs(n,root.right))
        return max(dbt(root.left),dbt(root.right),dfs(0,root.left)+dfs(0,root.right))
