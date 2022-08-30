class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=Counter(s)
        b=[]
        for i in s:
            if a[i]==1:
                b.append(i)
        if len(b)==0:
            return -1
        c=[]
        for i in range(len(b)):
            c.append(s.index(b[i]))
        return min(c)