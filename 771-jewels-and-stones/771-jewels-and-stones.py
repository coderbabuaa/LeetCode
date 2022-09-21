class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=Counter(stones)
        b=Counter(jewels)
        result = {key: a[key] for key in a if key in b}
        return sum(result.values())