import numpy as np
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(x) for a,x in enumerate(str(n))]
        return np.prod(np.array(res))-sum(res)