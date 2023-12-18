class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        temp = [0]*51
        for start, finish in ranges:
            temp[start-1] += 1
            temp[finish] -= 1
        for i in range(1, 51):
            temp[i] += temp[i-1]
        return 0 not in set(temp[left-1:right])