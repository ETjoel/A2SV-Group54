# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def helper(root):
            nonlocal res
            if not root:
                return []
            left = helper(root.left)
            if left and left[-1] >= root.val:
                res= False
            right = helper(root.right)
            if right and right[0] <= root.val:
                res = False
            return left + [root.val] + right
        helper(root)
        return res
            
            

