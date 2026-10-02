class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            curh = 0
            for p in piles:
                curh += math.ceil(p / mid)
            if curh <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res