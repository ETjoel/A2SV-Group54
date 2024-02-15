class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        res=0
        for char in s:
            if char == '(': stk.append('(')
            else:
                if stk: stk.pop()
                else:res+=1
        return res+len(stk)