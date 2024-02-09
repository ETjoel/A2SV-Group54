class Solution:
    def numberOfWays(self, s: str) -> int:
        pref_sum = list(map(int, s))
        for i in range(1, len(s)):
            pref_sum[i] += pref_sum[i-1]
        

        res, zeros, ones = 0, [0,0,0], [0,0,0]

        
        for i in range(len(s)):
            if s[i] == '1' and ones[1]:
                rest = pref_sum[i]
                rest -= pref_sum[ones[0]-1] if ones[0] > 0 else 0
                off = (i + 1 - ones[0]) - rest
                ones[2] += off * ones[1]
                res += ones[2]
                ones[0]=i; ones[1]+=1
            elif s[i] == '1':
                ones[0]=i; ones[1]+=1
            elif s[i] == '0' and zeros[1]:
                rest = pref_sum[i] - pref_sum[zeros[0]]
                zeros[2] += rest*zeros[1]
                res += zeros[2]
                zeros[0]=i; zeros[1]+=1
            elif s[i] == '0':
                zeros[0]=i; zeros[1]+=1
        return res