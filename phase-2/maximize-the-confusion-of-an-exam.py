class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = j = 0
        wind = {'T':0,'F':0}
        for i in range(len(answerKey)):
            wind[answerKey[i]]+=1
            while j < len(answerKey) and min(wind.values()) > k:
                wind[answerKey[j]]-=1
                j+=1
            res = max(sum(wind.values()), res)
        return res

            