#problem no.258- leetcode
#method 1 -
'''class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        return 1+(num-1)%9'''

#method 2-
class Solution:
    def addDigits(self,num:int) -> int: 
        while num>9:
            temp=0
            while num>0:
                temp+=num%10        
                num=num//10
            num=temp
        return num



  
