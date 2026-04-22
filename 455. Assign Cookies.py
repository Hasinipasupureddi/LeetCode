#455. Assign Cookies-leetcode
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()   # Sort greed factors of children
        s.sort()   # Sort cookie sizes
        child = 0
        cookies = 0
        while child < len(g) and cookies < len(s):
            if s[cookies] >= g[child]:  # If cookie satisfies child's greed
                child += 1              # Move to next child
            cookies += 1                # Move to next cookie
        return child
