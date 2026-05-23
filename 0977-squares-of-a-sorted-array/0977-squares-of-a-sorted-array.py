class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Create a result array of the same length
        res = [0] * n
        # Initialize two pointers
        left, right = 0, n - 1
        # Start filling the result array from the back
        pos = n - 1
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                res[pos] = left_square
                left += 1
            else:
                res[pos] = right_square
                right -= 1  
            pos -= 1  
        return res