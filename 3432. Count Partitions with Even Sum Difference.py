#3432. Count Partitions with Even Sum Difference- leetcode
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 2 == 0:
            return len(nums) - 1  
        else :
            return 0
