class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low=0
        high=len(s)
        ans=[]
        for i in range(len(s)):
            if s[i]=="I":
                ans.append(low)
                low+=1
            if s[i]=="D":
                ans.append(high)
                high-=1
        return ans+[low]