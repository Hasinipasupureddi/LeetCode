#342.power of four-leetcode
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return bool(0)
        while n%4==0:
            n=n//4
        return n==1
