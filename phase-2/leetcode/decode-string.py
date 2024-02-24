class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i] != ']':
                stk.append(s[i])
                print(i, s[i])
            elif s[i] == ']':
                char = ''
                while stk[-1] != '[':
                    char = stk.pop() + char
                stk.pop()
                mul = ''
                while len(stk) > 0 and stk[-1].isdigit():
                    mul = stk.pop() + mul
                stk.append(char * int(mul))
            i += 1
        return ''.join(stk)
            
            

#mul = [3]
#stk2 = [aaa, bcbc]
#stk = 
            
#3[acc]
#accaccacc