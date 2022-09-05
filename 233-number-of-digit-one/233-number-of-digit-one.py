class Solution:
    def countDigitOne(self, n):
        x, m, count = n, 1, 0
        while x > 0:
            lastDigit = x % 10
            x //= 10
            count += x * m
            if lastDigit == 1:
                count += n % m + 1
            elif lastDigit > 1:
                count += m
            m *= 10
        return count