class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        base = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        res = []
        def backtrack(s, i):
            if len(s) == len(digits):
                res.append(s)
                return
            
            for j in range(len(base[int(digits[i])])):
                s += base[int(digits[i])][j]
                backtrack(s,i+1)
                s = s[:-1]
        backtrack('',0)
        return res if res and res[0] != '' else []
