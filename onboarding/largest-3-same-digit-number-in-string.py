class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        for i in range(2, len(num)):
            if len(set(num[i-2:i+1])) == 1:
                ans = max(ans, num[i-2:i+1])
        return ans