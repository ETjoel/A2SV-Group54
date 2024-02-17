class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        res = 0
        for char in s:
            if stk and char == ')':
                top = stk.pop()
                if stk: 
                    stk[-1] += 2*top if top else 2
                else:
                    res+=top if top else 1
            else:
                stk.append(0)
        return res