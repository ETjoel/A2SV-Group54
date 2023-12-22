class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        rem = 0
        for i in range(len(digits)):
            if i == 0:
                digits[0] += 1
            else:
                if rem:
                    digits[i] += rem
                    rem -= 1
                else:
                    break
            if digits[i] == 10:
                digits[i] = 0; rem = 1
        if rem: digits.append(1)
        return reversed(digits)
            