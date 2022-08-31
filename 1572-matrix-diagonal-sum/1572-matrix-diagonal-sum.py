class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        p= 0
        s= 0
        n=len(mat)
        for i in range(0, n):
            p += mat[i][i]
            s += mat[i][n - i - 1]
        if n%2==0:
            return p+s
        else:
            return p+s-mat[math.ceil(n/2)-1][math.ceil(n/2)-1]