#problem number 242.valid anagram at leetcode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return Counter(s)==Counter(t) 
