class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        consecutive_count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                consecutive_count += 1
            else:
                if consecutive_count == k:
                    return True
                consecutive_count = 1  
        return consecutive_count == k