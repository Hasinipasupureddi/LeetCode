class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
        num_set = set(nums)
        ans = prefix_sum
        while ans in num_set:
            ans += 1

        return ans