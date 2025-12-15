#85. Maximal Rectangle-leetcode
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        maxArea = 0
        n = len(matrix[0])
        heights = [0] * n

        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))

        return maxArea  

    def largestRectangleArea(self, heights: List[int]) -> int:  # <-- Added self
        def findPSE(heights):
            n = len(heights)
            stack = []
            ans = [0] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                ans[i] = stack[-1] if stack else -1
                stack.append(i)
            return ans

        def findNSE(heights):
            n = len(heights)
            stack = []
            ans = [0] * n
            for i in range(n-1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                ans[i] = stack[-1] if stack else n
                stack.append(i)
            return ans

        n = len(heights)
        pse = findPSE(heights)
        nse = findNSE(heights)

        maxArea = 0
        for i in range(n):
            area = heights[i] * (nse[i] - pse[i] - 1)
            maxArea = max(area, maxArea)
        return maxArea
