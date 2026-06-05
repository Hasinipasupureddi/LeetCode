class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)
        # Case 1: Subarray size is 1
        if k == 1:
            ans = -1
            for num, freq in counts.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans 
        # Case 2: Subarray size is the full length of the array
        if k == n:
            return max(nums)
        # Case 3: 1 < k < n
        # Only the edge elements can belong to exactly one window
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[n - 1]] == 1:
            ans = max(ans, nums[n - 1])
        return ans