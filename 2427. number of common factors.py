#2427. number of common factors-leetcode
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        k = math.gcd(a, b)
        for i in range(1, int(k**0.5) + 1):
            if k % i == 0:
                count += 1
                if i != k // i:
                    count += 1
        return count
