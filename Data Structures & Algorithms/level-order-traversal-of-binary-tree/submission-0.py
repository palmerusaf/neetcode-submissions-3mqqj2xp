# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[root]
        res=[]
        while len(q):
            ql=len(q)
            lev=[]
            for i in range(ql):
                n=q[0]
                del q[0]
                if n:
                    lev.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if len(lev):
                res.append(lev)
        return res