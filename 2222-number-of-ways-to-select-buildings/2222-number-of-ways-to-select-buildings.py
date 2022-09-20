class Solution:
    def numberOfWays(self, s: str) -> int:
        noOf0, noOf1, noOf01, noOf10, res = 0, 0, 0, 0, 0
        for building in s:
            if building == '1':
                noOf1 += 1
                noOf01 += noOf0
                res += noOf10
            else:
                noOf0 += 1
                noOf10 += noOf1
                res += noOf01
        return res