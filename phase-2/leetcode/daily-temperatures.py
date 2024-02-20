class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stk = [0 for i in range(len(temperatures))], []
        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1][1]: 
                temp = stk.pop()
                res[temp[0]] = i - temp[0]
            stk.append((i, temperatures[i]))
        return res
        