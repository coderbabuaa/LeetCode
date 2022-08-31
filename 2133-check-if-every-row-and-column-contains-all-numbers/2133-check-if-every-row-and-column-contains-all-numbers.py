class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        a=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]<=len(matrix):
                    a.append(matrix[i][j])
            b=Counter(a)
            if len(b)!=len(a):
                return False
            else:
                a.clear()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[j][i]<=len(matrix):
                    a.append(matrix[j][i])
            b=Counter(a)
            if len(b)!=len(a):
                return False
            else:
                a.clear()
        return True