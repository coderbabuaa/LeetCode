def binary_search(nums, low, high, target):
            if high >= low:
                mid = (high + low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(nums, low, mid - 1, target)
                else:
                    return binary_search(nums, mid + 1, high, target)
            else:
                return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums,0,len(nums)-1,target)