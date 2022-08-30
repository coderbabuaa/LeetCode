class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for i in s:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] +=1
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1