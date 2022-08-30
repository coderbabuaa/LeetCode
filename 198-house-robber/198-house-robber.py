class Solution:
    def rob(self, nums: List[int]) -> int:
        sums = []
        for i in range(0,len(nums)):
            if i >2:
                to_sum = max(sums[:i-1])
            elif i == 2:
                to_sum = sums[0]
            else:
                to_sum = 0
            sums.append(nums[i] + to_sum)
        return max(sums)