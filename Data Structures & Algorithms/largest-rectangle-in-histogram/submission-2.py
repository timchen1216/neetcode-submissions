class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []                      # (起始索引, 高度)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = max(area, height * (i - idx))
                start = idx             # 繼承左邊界
            stack.append((start, h))

        n = len(heights)
        for idx, height in stack:       # 右邊沒有更矮的，延伸到底
            area = max(area, height * (n - idx))
        return area