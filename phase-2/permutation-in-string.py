class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        s1 = Counter(s1)
        wind = Counter(s2[:size])
        if s1 == wind: return 1
        for i in range(size, len(s2)):
            wind[s2[i-size]]-=1
            wind[s2[i]]+= 1
            if wind[s2[i-size]] <= 0: del wind[s2[i-size]]
            if s1 == wind: return 1
        return 0
