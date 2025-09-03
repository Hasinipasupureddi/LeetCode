#leetcode problem- 231 power of two
#using bit manipulation-
class Solution:
    def isPowerOfTwo(self,n:int) ->bool:
        if n==0:
            return False
        if(n&(n-1))==0:
            return True
        return False
#another method
'''class Solution:
    def isPowerOfTwo(self,n:int) ->bool:
        if n==0:
            return False
        while n%2==0:
            n=n//2
        if n==1:
            return True
        else:
            return False
          '''
