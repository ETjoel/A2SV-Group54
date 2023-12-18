
class Solution:
    def printVertically(self, s: str) -> List[str]:
        a, b, words = [], [], s.split()
        max_length = len(max(words, key=len))
        for i in words:
            if len(i) < max_length:
                i =  i + " " * (max_length - len(i)) 
            a.append(i)
        for i in zip(*a):
            b.append(''.join(i).rstrip())
        return b
#"AA  BBB C   DDDD EEEEE F"
#0,2 1,3  2,1 3,4  4,5.  5,1
#AA
#BB
#C 
#DD
#EE
#F
#
#