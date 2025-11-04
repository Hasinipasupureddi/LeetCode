#leetcode- problem 34. first and last position of element in sorted array-0(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        lower = self.lower_bound(nums, target)
        upper = self.upper_bound(nums, target)

        if lower == len(nums) or lower == -1 or nums[lower] != target:
            return [-1,-1]

        return [lower, upper-1]

        #alternate
        '''first_pos = self.lower_bound(nums, target)
        last_pos = self.upper_bound(nums, target) - 1

        if first_pos <= last_pos and last_pos < len(nums) and nums[first_pos] == target and nums[last_pos] == target:
            return [first_pos, last_pos]
        return [-1, -1]'''

        

    def lower_bound(self, array, target):
        left = 0
        right = len(array)-1
        ans = len(array)
        while left <= right:
            mid = (left + right)//2
            if array[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def upper_bound(self, array, target):
        left = 0
        right = len(array)-1
        ans = len(array)
        while left <= right:
            mid = (left + right)//2
            if array[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

        
