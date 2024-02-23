# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right) -> bool:
            if not left and not right:
                return True
            if left and right:
                if left.val != right.val:
                    return False
                fromLeft = symmetric(left.left, right.right)
                fromRight = symmetric(left.right, right.left)
                return fromLeft and fromRight
            else: return False
        return symmetric(root.left, root.right)