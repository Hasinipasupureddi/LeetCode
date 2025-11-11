#3658.GCD of odd and even sums-leetcode
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
       return gcd(n*n,n*(n+1)) 
