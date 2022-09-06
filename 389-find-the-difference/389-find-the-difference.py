class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            dic[c] -= 1
        for k in dic:
            if dic[k] != 0:
                return k