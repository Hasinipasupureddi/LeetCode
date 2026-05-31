class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = Counter(s)
        freqs = sorted(counts.values(), reverse=True)
        if len(freqs) <= k:
            return 0
        return sum(freqs[k:])