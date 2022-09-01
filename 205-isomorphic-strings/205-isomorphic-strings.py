class Solution:
    def isIsomorphic(self, s, t):
        # use two hash map to store map and reverse map while scanning both lists
        return len(set(zip(s,t)))==len(set(s))==len(set(t))