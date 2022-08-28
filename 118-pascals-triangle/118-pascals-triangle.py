class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1])
            for j in range(1,i+1):
                if j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])
        return res