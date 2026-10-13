class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timeMap[key]) - 1
        res = ""
        while l <= r :
            mid = (l + r) // 2 
            if self.timeMap[key][mid][0] <= timestamp:
                res = self.timeMap[key][mid][1]
            if self.timeMap[key][mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return res
    # (1, A), (3, B), (7, C), (10, D) 8
