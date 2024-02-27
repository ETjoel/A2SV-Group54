class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current,i):

            if i >= len(nums):
                res.append(current.copy())
                return 
            current.append(nums[i])
            backtrack(current,i + 1)
            current.pop()
            backtrack(current, i + 1)
        backtrack([],0)
        return res

