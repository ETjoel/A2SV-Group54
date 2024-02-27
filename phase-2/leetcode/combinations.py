class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(current,i):
            if len(current) == k:
                res.append(current[:])
                return
            
            for j in range(i,n+1):
                current.append(j)
                backtrack(current,j+1)
                current.pop()
        backtrack([],1)
        return res
            

            
