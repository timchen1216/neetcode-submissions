import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        for r, x in enumerate(nums):
            heapq.heappush(h, (-x, r))
            while h[0][1] <= r - k:          
                heapq.heappop(h)
            if r >= k - 1:
                res.append(-h[0][0])
        return res