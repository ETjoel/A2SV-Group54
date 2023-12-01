class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}
        for i in range(len(order)):
            index[order[i]] = i
        for i in range(1, len(words)):
            j = 0
            while j < len(words[i]) or j < len(words[i - 1]):
                if j < len(words[i]) and j < len(words[i - 1]):
                    if words[i][j] != words[i-1][j] and index[words[i-1][j]] > index[words[i][j]]:
                        print(words[i-1][j], words[i][j])
                        return False
                    elif words[i][j] != words[i-1][j] and index[words[i-1][j]] <index[words[i][j]]:
                        break
                elif j < len(words[i - 1]):
                    return False
                j += 1
            
        return True