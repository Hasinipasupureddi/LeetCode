class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, current_combo, total):
            if total == target:
                res.append(list(current_combo))
                return
            if i >= len(candidates) or total > target:
                return
            current_combo.append(candidates[i])
            backtrack(i, current_combo, total + candidates[i])
            current_combo.pop()
            backtrack(i + 1, current_combo, total)
        backtrack(0, [], 0)
        return res