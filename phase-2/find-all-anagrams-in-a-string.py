class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        target,window =Counter(p), Counter(s[:len_p])
        res = []
        if target == window: res.append(0)
        for i in range(1, len(s)-len_p+1):
            window[s[i-1]] -= 1
            if window[s[i-1]] <= 0: del window[s[i-1]]
            window[s[i+len_p-1]] += 1
            if target == window: res.append(i)
        return res
