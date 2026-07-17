class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(list(set(arr)))
        ranks = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        return [ranks[num] for num in arr]