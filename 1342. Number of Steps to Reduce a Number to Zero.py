#1342. Number of Steps to Reduce a Number to Zero-leetcode
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while n:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            steps += 1
        return steps
