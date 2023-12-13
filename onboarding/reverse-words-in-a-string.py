class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i].strip()
        return ' '.join([word for word in reversed(words) if word != ''])