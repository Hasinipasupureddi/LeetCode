#2114. Maximum Number of Words Found in Sentences-leetcode
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxwords = 0   
        for s in sentences:
            words = len(s.split())
            maxwords = max(maxwords, words)
        return maxwords
