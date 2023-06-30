# Runtime - 74.76% and Memory - 12.89%

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i+1] and target > nums[i]:
                return i+1