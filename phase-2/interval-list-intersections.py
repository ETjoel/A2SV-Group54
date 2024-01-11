class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # if not firstList or not secondList: return [[]]
        n_f, n_s = len(firstList), len(secondList)
        # pref = [0] * (max(firstList[n_f - 1][1], secondList[n_s - 1][1]) + 2)
        # for num in firstList:
        #     pref[num[0]] += 1
        #     pref[num[1] + 1] -= 1
        # for num in secondList:
        #     pref[num[0]] += 1
        #     pref[num[1] + 1] -= 1
        # for i in range(1, len(pref)):
        #     pref[i] += pref[i-1]
        # i, j = 0, 0
        # while i < len(pref) and j < len(pref):
            
        # return [[]]
        i, j = 0, 0
        res = []
        while i < n_f and j < n_s:
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if left <= right:
                res.append([left, right])
            if firstList[i][1] < secondList[j][1]:i+=1
            elif firstList[i][1] > secondList[j][1]:j+=1
            else: 
                i+=1;j+=1
        return res


            