class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counts = Counter(A[0]) 
        for word in A:
            counts &= Counter(word)
        res = []
        for letter, count in counts.items():
            res += [letter] * count
        return res