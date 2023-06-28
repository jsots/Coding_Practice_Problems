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