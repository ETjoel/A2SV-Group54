class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {s[i]:i for i in range(len(s))}
        res, interval,j = [],dic[s[0]],0
        for i in range(len(s)):
            if i == interval and dic[s[i]] == interval:
                interval+=1
                res.append(interval - j)
                j = interval
            if dic[s[i]] > interval:
                interval = dic[s[i]]
        return res
            
