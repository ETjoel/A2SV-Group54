class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        num = n
        while num not in dic:
            temp = 0
            for s in str(num):
                temp += int(s) ** 2
            if temp in [1,10, 100]:
                return True
            dic[num] = temp
            num = temp
        return False