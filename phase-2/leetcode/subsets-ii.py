class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(current,i):
            res.add(tuple(sorted(current)))

            if i >= len(nums):
                return 
            current.append(nums[i])
            backtrack(current,i + 1)
            current.pop()
            backtrack(current, i + 1)
        backtrack([],0)
        return res