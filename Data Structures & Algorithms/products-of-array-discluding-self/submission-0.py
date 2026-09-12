class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for x in nums[:-1] :
            prefix.append(prefix[-1]*x)
        for y in nums[:0:-1]:
            suffix.append(suffix[-1]*y)
        suffix.reverse()
        res = [x*y for x, y in zip(prefix,suffix)]
        return res