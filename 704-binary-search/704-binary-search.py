class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target: return mid
            if target>nums[mid]: low = mid+1
            else: high = mid-1
        return -1