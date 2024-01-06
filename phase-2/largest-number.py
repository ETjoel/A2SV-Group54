from typing import List
from functools import cmp_to_key

class Solution:
    def loxiological(self, a: str, b: str):
        j = 0
        while j < min(len(a), len(b)) :
            if a[j] > b[j] or a[j] < b[j]:
                return 1 if a[j] > b[j]  else -1
            j += 1
        if len(a) > len(b):
            return  self.loxiological(a[j:len(a)], b)
        elif len(b) > len(a):
            print(a, b[j:len(b)])
            return  self.loxiological(a, b[j:len(b)])
        else:
            return 0
    def largestNumber(self, nums: List[int]) -> str:
        s = list(map(str, nums))
        # for i in range(len(s) - 1):
        #     print(self.loxiological(s[i], s[i + 1]))
        s.sort(key=cmp_to_key(self.loxiological), reverse = True)
        return str(int(''.join(s)))
        
        