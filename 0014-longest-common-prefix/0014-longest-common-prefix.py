class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ''' # Edge case: if the input list is empty, return an empty string
        if not strs:
            return ""
        # Use the first string as our baseline reference
        base = strs[0]
        # Iterate through every character index of the base string
        for i in range(len(base)):
            # Compare the character 'base[i]' with the same position in all other strings
            for word in strs[1:]:
                # If the current word is shorter than index 'i',
                # or if the character doesn't match, we've found our boundary
                if i == len(word) or word[i] != base[i]:
                    return base[:i] # Return the prefix sliced up to index i
                    
        return base'''
        if not strs:
            return ""
            
        # Find lexicographically lowest and highest strings
        first = min(strs)
        last = max(strs)
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return first[:i]
                
        return first