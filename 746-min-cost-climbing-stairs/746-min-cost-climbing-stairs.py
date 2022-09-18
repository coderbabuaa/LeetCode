class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        for i in range(2,len(cost)):
            temp = cost[i] + min(prev2, prev1)
            prev2 = prev1
            prev1 = temp
        return min(prev2, prev1)