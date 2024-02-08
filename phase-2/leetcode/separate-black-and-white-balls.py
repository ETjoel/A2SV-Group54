class Solution:
    def minimumSteps(self, s: str) -> int:
        res = one = 0
        for bit in s:
            if bit == '1': one+=1
            else: res+=one
        return res