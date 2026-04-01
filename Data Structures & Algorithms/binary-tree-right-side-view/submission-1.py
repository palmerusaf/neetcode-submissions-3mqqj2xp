# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res=[]
        q=[root]
        while q:
            level_size = len(q)

            for i in range(level_size):
                c = q[0]
                del q[0]

                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)

                if i == level_size - 1:
                    res.append(c.val)
        return res