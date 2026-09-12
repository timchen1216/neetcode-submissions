class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for x in numSet:
            if x - 1 not in numSet:
                length = 1
                while x + length in numSet:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen