class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        base = [1,2,3,4,5,6,7,8,9]
        res = []
        def backtrack(curr, i):
            if sum(curr) == n and len(curr) == k:
                res.append(curr[:])
                return 
            if i >= len(base) or len(curr) >= k:
                return

            curr.append(base[i])
            backtrack(curr, i+1)
            curr.pop()
            backtrack(curr, i+1)
        backtrack([],0)
        return res
            