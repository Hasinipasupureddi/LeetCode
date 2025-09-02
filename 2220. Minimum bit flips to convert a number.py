#minimum bit flips to convert a number- leet code prob- 2220

class Solution:
    def minBitFlips(self,start:int,goal:int)->int:
        a=start^goal
        return bin(a).count("1")
