class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        int_part = ""
        num, denom = numerator, denominator
        if num * denom < 0: int_part += '-'
        num, denom = abs(num), abs(denom)
        int_part += str(num // denom)
        if num % denom == 0: return int_part
        dec_part = ""
        d = dict()
        i = 0
        while True:
            num %= denom
            if num == 0: return int_part + '.' + dec_part
            elif num in d: return "{}.{}({})".format(int_part, dec_part[:d[num]], dec_part[d[num]:])
            d[num] = i
            i += 1
            num *= 10
            dec_part += str(num // denom)