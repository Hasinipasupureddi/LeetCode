#13. Roman to Integer-leetcode
class Solution:
    def romanToInt(self, s: str) -> int:
        val = [0] * 91
        val[73] = 1      # I
        val[86] = 5      # V
        val[88] = 10     # X
        val[76] = 50     # L
        val[67] = 100    # C
        val[68] = 500    # D
        val[77] = 1000   # M

        total = 0
        n = len(s)
        
        for i in range(n - 1):
            if val[ord(s[i])] < val[ord(s[i+1])]:
                total -= val[ord(s[i])]
            else:
                total += val[ord(s[i])]

        total += val[ord(s[-1])]
        return total
