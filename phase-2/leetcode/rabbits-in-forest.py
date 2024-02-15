class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        res = 0
        for rab in answers:
            if dic.get(rab,0):
                dic[rab]-=1
            else:
                dic[rab] = rab
                res+=rab+1
        return res