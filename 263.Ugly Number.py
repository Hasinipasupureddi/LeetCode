#263.Ugly Number-leetcode
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for m in [2, 3, 5]:
            while n % m == 0:
                n //= m
        return n == 1 
