# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        def helper(root,row, col):
            nonlocal dic
            if not root:
                return None
            
            dic[(row, col)] = dic.get((row, col), []) + [root.val]
            helper(root.left,row+1, col-1)
            helper(root.right,row+1, col+1)
        
        helper(root,0,0)
        
        res = {}
        for key in sorted(dic.keys(), key = lambda x: (x[1],x[0])):
            dic[key].sort()
            res[key[1]] = res.get(key[1], []) + dic[key]
        return [(res[key]) for key in sorted(res.keys())]