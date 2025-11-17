#628. Maximum Product of Three Numbers
'''class Solution:
    def maximumProduct(self, nums: List[int]) -> int: 
        nums.sort()
        # Option 1: Product of three largest numbers
        option1 = nums[-1] * nums[-2] * nums[-3]
        # Option 2: Product of two smallest and largest number
        option2 = nums[0] * nums[1] * nums[-1]
        return max(option1, option2)'''

#optimixed code
class Solution:
    def maximumProduct(self, nums: List[int]) -> int: 
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')    
        for x in nums:
            # update max values
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x
            # update min values
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
        return max(max1*max2*max3, min1*min2*max1)
