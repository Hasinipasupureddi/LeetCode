#1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 0
        b = 1
        while n > 0:
            digit = n % 10
            a += digit
            b *= digit
            n //= 10
        return b - a
