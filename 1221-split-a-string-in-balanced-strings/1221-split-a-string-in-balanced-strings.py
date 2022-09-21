class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r,ans=0,0
        for c in s:
            if c=='R':
                r+=1
            else:
                r-=1
            if r==0:
                ans+=1
        return ans