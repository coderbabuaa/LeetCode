class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        a=math.log(n,4)
        if pow(4,math.floor(a))==n:
            return True
        return False