class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        t = [(names[i], heights[i]) for i in range(n)]
        for i in range(n):
            for j in range(n-1):
                if t[j][1] < t[j+1][1]:
                    t[j], t[j+1] = t[j+1], t[j]
        return [c[0] for c in t]