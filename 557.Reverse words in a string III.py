#557.Reverse words in a string III-leetcode
class Solution:
    def reverseWords(self, s: str) -> str:
        p=s.split()
        p=[i[::-1]for i in p]
        return " ".join(p)
