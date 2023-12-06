class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keys = dict.fromkeys('qwertyuiop', 1) | dict.fromkeys('asdfghjkl', 2) | dict.fromkeys('zxcvbnm', 3)
        ans = []
        for word in words:
            ans.append(word)
            for j in range(1, len(word)):
                if keys[word[j].lower()] != keys[word[j-1].lower()]:
                    ans.pop()
                    break
            print(ans)
        return ans