class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n, m = len(arr1), len(arr2)
        indexes = {arr2[i]:i for i in range(m)}
        arr1.sort(key = lambda x: indexes.get(x, m))
        j = n-1
        while arr1[j] not in indexes:
            j -= 1
        arr1[j+1:] = sorted(arr1[j+1:])
        return arr1