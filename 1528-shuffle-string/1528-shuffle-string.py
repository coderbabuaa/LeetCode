class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a={}
        for i in range(len(indices)):
            a[indices[i]]=s[i]
        dic=OrderedDict(sorted(a.items()))
        ans=""
        for j in range(len(indices)):
            ans+=dic[j]
        return ans
        