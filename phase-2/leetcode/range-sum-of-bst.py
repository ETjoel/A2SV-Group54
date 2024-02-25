# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val >= low and root.val <= high:
            left = self.rangeSumBST(root.left,low, high) if root.val > low else 0
            right = self.rangeSumBST(root.right,low, high) if root.val < high else 0
            return left + right + root.val
        elif root.val < low:
            return self.rangeSumBST(root.right,low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left,low, high) 
        else: return 0