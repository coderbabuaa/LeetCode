class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=Counter(ransomNote)
        b=Counter(magazine)
        for i in ransomNote:
            if a[i]>b[i]:
                return False
        return True