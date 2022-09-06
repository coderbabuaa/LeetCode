class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=Counter(nums)
        ans=0
        for i in a:
            if a[i]>1:
                ans+=comb(a[i],2)
        return ans