class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return set(edges[0]).intersection(edges[1]).pop()