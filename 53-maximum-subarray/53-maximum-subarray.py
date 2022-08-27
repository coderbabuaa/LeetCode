class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = 0
        max_ending_here = 0
       #kadanes algorithm
        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0   
        if max_so_far>0:
            return max_so_far
        else:
            return max(nums)#if all the elements are negative print the maximun element