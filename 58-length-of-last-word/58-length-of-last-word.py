class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.split()
        return len(str[len(str)-1])