class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[len(nums)-1],nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3])