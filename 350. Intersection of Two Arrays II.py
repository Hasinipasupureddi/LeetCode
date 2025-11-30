#350. Intersection of Two Arrays II-leetcode
from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        ans = []
        append = ans.append
        get = c1.get
        for x in nums2:
            if get(x, 0) > 0:
                append(x)
                c1[x] -= 1
        return ans
