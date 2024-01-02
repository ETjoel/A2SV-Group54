class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall('[a-zA-Z0-9]', s)).strip().lower()
        print(s)
        j = len(s)-1
        for i in range(len(s)//2):
            if s[i] != s[j]: return False
            j -= 1
        return True