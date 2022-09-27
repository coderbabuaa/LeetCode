class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [True if x + extraCandies >= max(candies) else False for x in candies]
        