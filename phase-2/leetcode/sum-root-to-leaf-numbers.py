# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return []

            left = helper(root.left)
            right = helper(root.right)

            for i in range(len(left)):
                left[i] = f'{root.val}' + left[i]
            for i in range(len(right)):
                right[i] = f'{root.val}' + right[i]
            if not left and not right:
                return [f'{root.val}']
            return left + right
        print(helper(root))
        return sum(map(int,helper(root) ))
            

        