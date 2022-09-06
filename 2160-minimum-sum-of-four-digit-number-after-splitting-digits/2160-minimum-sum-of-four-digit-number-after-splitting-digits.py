class Solution:
    def minimumSum(self, num: int) -> int:
        n=str(num)
        res=[]
        for i in n:
            res.append(int(i))
        res.sort()
        num1=res[0]*10+res[3]
        num2=res[1]*10+res[2]
        return (num1+num2)