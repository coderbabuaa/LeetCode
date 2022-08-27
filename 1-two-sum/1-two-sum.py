class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
           
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i 