class Solution:
    def freqAlphabets(self, s: str) -> str:
        a = s.split('#')
        n = len(a)
        ans = []
        for i in range(n):
            if i != n - 1:
                ans += list(a[i])
                temp = ans.pop()
                ans[-1] += temp
            else:
                ans += list(a[i])
        word = ''
        for num in ans:
            word += chr(ord('a') + int(num) - 1)
        return word