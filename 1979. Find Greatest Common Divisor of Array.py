#1979. Find Greatest Common Divisor of Array-leetcode
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        return math.gcd(a,b)
