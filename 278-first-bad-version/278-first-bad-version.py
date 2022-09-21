# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s=0
        l=n
        while s<l:
            mid = s+(l-s)/2
            if isBadVersion(mid):
                l=mid
            else:
                s=mid+1
        return int(s)