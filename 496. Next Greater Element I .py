#496. Next Greater Element I-leetcode
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(x, -1) for x in nums1]

''' #or alternate
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            found = False
            for num in nums2[nums2.index(x)+1:]:
                if num > x:
                    res.append(num)
                    found = True
                    break
            if not found:
                res.append(-1)
        return res
'''
