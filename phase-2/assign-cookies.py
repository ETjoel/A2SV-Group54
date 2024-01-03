class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=ans =0
        for i in range(len(g)):
            while j < len(s) and g[i] > s[j]:j += 1
            if j<len(s) and g[i] <= s[j]:
                ans+=1;j+=1
        return ans