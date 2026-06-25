# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        if (root.val != subRoot.val) :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, q, r):
        if not q and not r:
            return True
        if not q or not r or q.val != r.val:
            return False

        return self.sameTree(q.left, r.left) and self.sameTree(q.right, r.right)