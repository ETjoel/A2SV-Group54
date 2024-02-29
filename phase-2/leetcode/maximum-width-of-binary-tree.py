# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = {}
        def helper(root, level):
            nonlocal dic
            if not root:  
                for key in dic:
                    if key >= level:
                        dic[key][1] += (1 * (pow(2, key - level)))
                return

            left = helper(root.left,level+1)
            right = helper(root.right, level+1)
            if level in dic:
                dic[level][0] += 1+ dic[level][1]
                dic[level][1] = 0
            else:
                dic[level] = [1,0]
        helper(root, 0)
        return max(dic.values() , key = lambda x : x[0])[0]