class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        se = set(s)
        odd=even=countodd = 0
        for i in se:
            if d[i]%2 == 0:
                even+=d[i]
            elif d[i]%2!=0:
                odd+=d[i]
                countodd+=1
        if odd>0:
            return (even+odd)-(countodd-1)
        elif even>0 and odd==0:
            return even