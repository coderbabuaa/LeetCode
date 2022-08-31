class Solution:
    def shuffle(self, nums, n):
        ans=[]
        for i in range(n):
            ans.append(nums[i])   
            ans.append(nums[n+i])
        return ans