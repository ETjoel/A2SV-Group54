class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2 = 0,0
        for i, st in enumerate(num1):
            n1 = n1 * (10) + int(st)
        for i, st in enumerate(num2):
            n2 = n2 * (10) + int(st)
        print(n1, n2)
        return str(n1 * n2)