class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        j = 0
        while j < len(command):
            if command[j] == 'G':
                ans += 'G'
            else:
                i = j
                while command[j] != ')':
                    j += 1
                temp = command[i:j+1]
                if temp == '()':
                    ans += 'o'
                else:
                    ans += 'al'
            j += 1
        return ans