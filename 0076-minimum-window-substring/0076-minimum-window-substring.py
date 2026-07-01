from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. Count what we need
        needed = Counter(t)
        missing = len(t)  # Total number of characters we still need to find
        
        left = 0
        start, end = 0, float('inf')
        
        # 2. Expand the right pointer
        for right, char in enumerate(s):
            # If this is a character we are looking for, decrease the missing count
            if needed[char] > 0:
                missing -= 1
            # Decrease its count in our requirements dictionary
            needed[char] -= 1
            
            # 3. If we have found all characters, try to shrink from the left
            while missing == 0:
                # Update our best window if this one is smaller
                if right - left < end - start:
                    start, end = left, right
                
                # We are about to slide past s[left], so put it back into requirements
                left_char = s[left]
                needed[left_char] += 1
                
                # If it's a character from 't' and we actually need it now, update missing
                if needed[left_char] > 0:
                    missing += 1
                
                left += 1
                
        return s[start:end+1] if end != float('inf') else ""