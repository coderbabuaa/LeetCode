class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        p= 0
        n=len(mat)
        for i in range(0, n):
            p += mat[i][i]+mat[i][n - i - 1]
        if n%2==0:
            return p
        else:
            return p-mat[math.ceil(n/2)-1][math.ceil(n/2)-1]