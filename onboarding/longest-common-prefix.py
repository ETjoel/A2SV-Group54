class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for st in strs:
            j = 0
            while j < len(common) and j < len(st):
                if common[j] != st[j]: break
                j += 1
            common = common[:j]
        print(common)
        return common
            