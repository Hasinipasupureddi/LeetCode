class Solution:
    def check(self, nums: List[int]) -> bool:
        count_drops = 0
        n = len(nums)
        
        for i in range(n):
            # Check if the current element is greater than the next element (cyclically)
            if nums[i] > nums[(i + 1) % n]:
                count_drops += 1
                
            # If we find more than one drop, it's impossible to be a sorted rotated array
            if count_drops > 1:
                return False
                
        return True