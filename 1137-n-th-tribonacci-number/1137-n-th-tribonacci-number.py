class Solution:
    def tribonacci(self, n: int) -> int:
        F=[0,1,1]
        for i in range(3,n+1):
            F.append(F[i-2]+F[i-1]+F[i-3])
        return F[n]