#1935.Maximum Number of words you can type-leetcode
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int: 
        broken=set(brokenLetters)
        count=0
        for i in text.split():
            if not(set(i) & broken):
                count+=1
        return count
        
