class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a = ''.join(filter(str.isalnum, s))
        b=a.replace(" ", "")
        return b == b[::-1]