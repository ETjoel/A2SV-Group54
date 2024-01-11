class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        n = m = 0
        while i < len(name) and n < len(typed):
            while j < len(name) and  name[i] == name[j]:j+=1
            while m < len(typed) and name[i] == typed[m]:m+=1
            if j -i > m - n: return False
            i = j;n = m
            if (m >= len(typed) and i < len(name)) or (i >= len(name) and m < len(typed)): return False
        print(i, j, m,n)
        # if m < len(typed) and name[i-1] != typed[m]: return False
        # elif name[i-1] != typed[m-1]: return False
        return True