# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root.left and root.right:
            return root.left.val < root.val and root.val < root.right.val and self.isValidBST(root.left) and self.isValidBST(root.right)
        if root.left:
            return root.left.val < root.val and self.isValidBST(root.left)
        if root.right:
            return root.left.right > root.val and self.isValidBST(root.right)
        
        return True