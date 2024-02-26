# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, nums):
            if not root:
                return
            nums.append(root.val)
            dfs(root.left, nums)
            dfs(root.right, nums)
            return nums
        counter = Counter(dfs(root,[]))
        print(counter)
        mode = max(counter.values())
        return [key for key in counter if counter[key] == mode]