class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        fs = [0]*(n+1)
        fs[1] = 1
        fs[2] = 2
        #fibonacci sequence
        for i in range(3,n+1):
            fs[i] = fs[i-1]+fs[i-2]
        return fs[n]