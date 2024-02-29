class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def backtrack(curr, i):
            if sum(curr) == target:
                res.add(tuple(curr))
                return
            if sum(curr) > target or i >= len(candidates):
                return
            
            
            curr.append(candidates[i])
            backtrack(curr, i+1)
            curr.pop()
            while i < len(candidates)-1 and candidates[i]==candidates[i+1]:i+=1
            backtrack(curr,i+1)
        backtrack([],0)
        return res