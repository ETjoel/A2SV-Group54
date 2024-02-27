# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        #it is TLE don't submitt
        res = 0
        def BST(root):
            nonlocal res
            if not root:
                return []
            
            left = BST(root.left)
            right = BST(root.right)
            
            if (left and left[-1] >= root.val) or (right and right[0] <= root.val):
                return [-float('inf')]

            temp = left + [root.val] + right
            res = max(res, sum(temp))
            return temp
        temp = BST(root)
        print(temp)
        return res