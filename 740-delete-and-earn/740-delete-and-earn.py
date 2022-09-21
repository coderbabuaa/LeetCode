from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int: 
        points = defaultdict(int)
        maxNum = 0
        for num in nums:
            points[num] += num
            maxNum = max(maxNum, num)
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return points[1]
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + points[i])
            return memo[i]
        return dp(maxNum)