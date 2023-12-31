class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        j = 0
        while j < len(word1) and j < len(word2):
            merged += word1[j] + word2[j]
            j += 1
        if j < len(word1):
            merged += word1[j:]
        if j < len(word2):
            merged += word2[j:]
        return merged