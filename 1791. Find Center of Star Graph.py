#1791. Find Center of Star Graph-leetcode
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]
        return a if a in (c, d) else b
