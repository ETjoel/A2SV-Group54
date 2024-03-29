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