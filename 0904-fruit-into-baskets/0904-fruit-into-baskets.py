class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        freq = {}
        ans = 0
        for r in range(len(fruits)):
            if fruits[r] in freq:
                freq[fruits[r]] += 1
            else:
                freq[fruits[r]] = 1
            while len(freq) > 2:   # shrink window if >2 types
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            ans = max(ans, r - left + 1)
        return ans