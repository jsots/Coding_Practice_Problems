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


# Runtime - 34.32% and Memory - 69.25%

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


# Did it again, on another date.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_once = set()
        for num in nums:
            if num not in seen_once:
                seen_once.add(num)
            else:
                return True
        return False