# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root) -> List[List[int]]:
            if not root:
                return [[]]

            left = helper(root.left)
            right = helper(root.right)

            i, j = 0, 0
            while i < len(left) and j < len(right):
                left[i]+=right[i]
                i+=1;j+=1
            if j < len(right):
                left+= right[j:]
        
            return [[root.val]] + left


        res = helper(root) 
        for i in range(len(res)):
            if i % 2:
                res[i] = res[i][::-1]
        while res and res[-1] == []:
            res.pop()
        return res

        