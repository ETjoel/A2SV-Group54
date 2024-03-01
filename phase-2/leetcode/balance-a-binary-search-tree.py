# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            
            middle = math.ceil((right + left)/2)
            leftNode = helper(left, middle - 1)
            rightNode = helper(middle+1,right)

            return TreeNode(nums[middle], leftNode,rightNode)
        return helper(0, len(nums)-1)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root: Optional[TreeNode], res: List[int]) -> List[int]:
            if not root:
                return res
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
            return res
        return inorder(root, [])
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.sortedArrayToBST(self.inorderTraversal(root))