class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n

        stack = [] 
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)
        
        stack = []
        for i, h in reversed(list(enumerate(heights))):
            while stack and h < heights[stack[-1]]:
                idx = stack.pop()
                left[idx] = i
            stack.append(i)
        
        area = 0
        for i, h in enumerate(heights):
            curArea = h * (right[i] - left[i] - 1)
            area = max(area, curArea)
        return area