class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:      
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                cur = nums[j] + nums[k]
                if cur < -x:
                    j += 1
                elif cur > -x:
                    k -= 1
                else:
                    res.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:   
                        j += 1
        return res