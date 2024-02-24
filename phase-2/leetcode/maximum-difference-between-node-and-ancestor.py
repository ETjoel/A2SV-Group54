# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return [0,float('inf'),0]

            left = helper(root.left)
            right = helper(root.right)

            maxim = max(root.val, left[0], right[0])
            minim = min(root.val, left[1], right[1])
            v = abs(root.val - maxim)
            v = max(v, abs(root.val - minim))
            v = max(v, left[2], right[2])

            return [maxim, minim, v]
        return helper(root)[2]
            