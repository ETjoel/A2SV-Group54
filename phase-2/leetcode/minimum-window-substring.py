class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        counter_wind = {}
        i ,last = 0, float('inf')
        for key in counter_t:
            while i < len(s) and  counter_wind.get(key, 0) < counter_t[key]:
                if s[i] in counter_t:
                    last = min(last, i)
                    counter_wind[s[i]] = counter_wind.get(s[i], 0)+1
                i+=1
            if i >= len(s) and counter_wind.get(key, 0) < counter_t[key]:
                return ''
            while last < len(s) and  s[last] not in counter_t or counter_wind[s[last]] > counter_t[s[last]]:
                if s[last] in counter_wind:
                    counter_wind[s[last]]-=1
                last+=1
        res = s[last:i]
        for j in range(i, len(s)):
            if s[j] in counter_t:
                counter_wind[s[j]] = counter_wind.get(s[j], 0)+1
            while s[last] not in counter_t or counter_wind[s[last]] > counter_t[s[last]]:
                if s[last] in counter_wind:
                    counter_wind[s[last]]-=1
                last+=1
            if j + 1- last < len(res):
                res = s[last:j+1]
        return res

        