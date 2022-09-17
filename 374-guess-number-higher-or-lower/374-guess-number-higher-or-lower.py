class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while True:   
            m = (low+high) // 2
            if guess(m) == 0: return m
            elif guess(m) == 1: low = m+1
            else: high = m-1