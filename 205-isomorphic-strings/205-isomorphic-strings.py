class Solution:
    def isIsomorphic(self, s, t):
        # use two hash map to store map and reverse map while scanning both lists
        letter_map = {}
        reverse_map = {}
        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            if letter_s in letter_map and letter_map[letter_s] != letter_t:
                return False
            if letter_t in reverse_map and reverse_map[letter_t] != letter_s:
                return False
            letter_map[letter_s] = letter_t
            reverse_map[letter_t] = letter_s
        return True