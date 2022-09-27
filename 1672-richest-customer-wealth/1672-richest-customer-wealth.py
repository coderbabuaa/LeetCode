class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(cus) for cus in accounts])