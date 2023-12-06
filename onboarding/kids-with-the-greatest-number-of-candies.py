class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _greatest = max(candies)
        return [True if kid + extraCandies >= _greatest else False for kid in candies]