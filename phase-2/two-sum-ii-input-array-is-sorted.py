class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        j = n - 1
        for i in range(n):
            temp = numbers[i] + numbers[j]
            if temp == target:
                return  [i + 1, j + 1]
            elif temp >= target:
                while j > i and temp >= target:
                    if temp == target:
                        return  [i + 1, j + 1]
                    j -= 1
                    temp = numbers[i] + numbers[j]
        return [0,0]