#2197. replace non-coprime numbers in array-leetcode
from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for num in nums:
            stack.append(num)
            while len(stack)>=2 and gcd(stack[-1],stack[-2])>1:
                a=stack.pop()
                b=stack.pop()
                l=a*b//gcd(a,b)
                stack.append(l)
        return stack
