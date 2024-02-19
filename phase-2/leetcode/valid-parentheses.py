class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if stk and (stk[-1] == '[' and char == ']'):stk.pop()
            elif stk and (stk[-1] == '(' and char == ')'):stk.pop()
            elif stk and (stk[-1] == '{' and char == '}'):stk.pop()
            else:
                stk.append(char)
        print(stk)
        return len(stk) == 0
                