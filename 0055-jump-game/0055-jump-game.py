class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:   # If current index is unreachable
                return False
            max_reach = max(max_reach, i + nums[i])  # Update max reachable index
        return True