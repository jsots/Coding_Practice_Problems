# Runtime - 5.19% and Memory - 6.92%

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        unique_nums = {}
        for i in range(0, len(nums)):
            if nums[i] in unique_nums:
                return True
            else:
                unique_nums[nums[i]] = 1
        return False


# Runtime - 7.60% and Memory - 93.25%

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False