class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        if nums.count(0)>1:
            return True
        elif sum(a)==sum(nums):
            return False
        else:
            return True
            