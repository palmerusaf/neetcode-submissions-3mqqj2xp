# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def p(r):
            if not r:return 'N'
            return str(r.val)+' '+p(r.left)+' '+p(r.right)
        return p(root)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        d=data.split(' ')
        def f():
            if d[0] =='N':
                del d[0]
                return None
            r=TreeNode(val=int(d[0]))
            del d[0]
            r.left=f()
            r.right=f()
            return r
        return f()