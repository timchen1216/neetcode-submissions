class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] < target and nums[mid] >= nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target and nums[mid] <= nums[-1]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1