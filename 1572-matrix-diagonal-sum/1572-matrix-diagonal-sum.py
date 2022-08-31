class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i == j) or (j == len(mat) - 1 - i):
                    sum += mat[i][j]
                
        return sum