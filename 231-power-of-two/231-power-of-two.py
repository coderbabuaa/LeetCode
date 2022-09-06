class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        a=math.log(n,2)
        if pow(2,math.floor(a))==n:
            return True
        return False