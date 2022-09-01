class Solution:
    def isIsomorphic(self, s, t):
        return len(set(zip(s,t)))==len(set(s))==len(set(t))