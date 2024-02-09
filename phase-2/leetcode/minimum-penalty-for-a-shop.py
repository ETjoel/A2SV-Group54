class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref = [0]
        totY = totN = 0
        for i in customers:
            if i == 'Y':
                pref.append(1)
                totY+=1
            else:
                pref.append(0)
                totN+=1
        for i in range(1,len(pref)):
            pref[i] = pref[i-1] + pref[i]

        tempIndex = 0
        tempPenalty = float("inf")

        for i in range(len(pref)):
            leftY = pref[i]
            leftN = (i) - pref[i]
            rightY = totY - leftY
            if tempPenalty > (leftN + rightY):
                tempIndex = i
                tempPenalty = leftN + rightY
        return tempIndex