#1281.Subtract the product and sum of digits of an integer-leetcode
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 1
        b = 0
        while n > 0:
            digit = n % 10
            a *= digit
            b += digit
            n //= 10
        return a - b
