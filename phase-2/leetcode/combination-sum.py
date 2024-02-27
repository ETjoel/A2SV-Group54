class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr, i):
            nonlocal res
            if sum(curr) == target:
                res.append(curr[:])
                return
            elif i >= len(candidates) or  sum(curr) > target:
                return

            curr.append(candidates[i])
            backtrack(curr,i)
            curr.pop()
            backtrack(curr,i+1)
        backtrack([],0)
        return res